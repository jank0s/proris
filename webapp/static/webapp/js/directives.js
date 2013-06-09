App.directive('piechart', function() {
    return {
        restrict: 'EA',
        link: function(scope, elem, attrs, $window) {
            var data = scope[attrs.ngModel];
            var chart = null;
            
            scope.$watch(attrs.ngModel, function(v){
                if(!chart){
                    chart = $.plot(elem, v , {
	     		           series: {
	   				        pie: {
	   				            show: true,
	   				            radius: 1000,
	   				            label: {
	   				            	show: false
	   				            }
	   				        }
	   				    },
	   				    legend: {
	   				        show: false
	   				    },
	   				    grid: {
	   				        hoverable: true,
	   				        clickable: true
	   				    }
                    });
                    elem.show();
                }else{
                    chart.setData(v);
                    chart.setupGrid();
                    chart.draw();
                }
            });
                       
            
            var previousPoint = null; 
            elem.bind("plothover", function(event, pos, obj) {

				if (!obj) {
					$("#tooltip").remove();
					return;
				}
				
				if (previousPoint != obj.datapoint) { 
                    previousPoint = obj.datapoint; 
                    $("#tooltip").remove(); 
                 
					$('<div id="tooltip">' + obj.series.label +'</div>').css( { 
				            position: 'absolute', 
				            display: 'none', 
				            top: pos.pageY + 5, 
				            left: pos.pageX + 5, 
				            border: '1px solid #fdd', 
				            padding: '2px',
				            'background-color': '#fee', 
				            opacity: 0.80 
				        }).appendTo("body").fadeIn(200); 
			    }

			});
			
            
            //elem.show();
        }
    };
});

App.directive('smallpiechart', function() {
    return {
        restrict: 'EA',
        link: function(scope, elem, attrs, $window) {
            var data = scope[attrs.ngModel];
            var chart = null;
            
            scope.$watch(attrs.ngModel, function(v){
                if(!chart){
                    chart = $.plot(elem, v , {
	     		           series: {
	   				        pie: {
	   				            show: true,
	   				            radius: 150,
	   				            label: {
	   				            	show: false
	   				            }
	   				        }
	   				    },
	   				    legend: {
	   				        show: false
	   				    },
	   				    grid: {
	   				        hoverable: true,
	   				        clickable: true
	   				    }
                    });
                    elem.show();
                }else{
                    chart.setData(v);
                    chart.setupGrid();
                    chart.draw();
                }
            });
                       
            
            var previousPoint = null; 
            elem.bind("plothover", function(event, pos, obj) {

				if (!obj) {
					$("#tooltip").remove();
					return;
				}
				
				if (previousPoint != obj.datapoint) { 
                    previousPoint = obj.datapoint; 
                    $("#tooltip").remove(); 
                 
					$('<div id="tooltip">' + obj.series.label +'</div>').css( { 
				            position: 'absolute', 
				            display: 'none', 
				            top: pos.pageY + 5, 
				            left: pos.pageX + 5, 
				            border: '1px solid #fdd', 
				            padding: '2px',
				            'background-color': '#fee', 
				            opacity: 0.80 
				        }).appendTo("body").fadeIn(200); 
			    }

			});
			
            
            //elem.show();
        }
    };
});

App.directive('barchart', function() {
    return {
        restrict: 'EA',
        link: function(scope, elem, attrs, $window) {
            var data = scope[attrs.ngModel];
            var chart = null;
            
            scope.$watch(attrs.ngModel, function(v){
                if(!chart){
                    chart = $.plot(elem, v , {
            			series: {
            				bars: {
            					show: true,
            					barWidth: 0.5,
            					align: "center",
            					label: {
	   				            	show: false
	   				            }
            				}
            			},
            			xaxis: {
            				mode: "categories",
            				tickLength: 20
            			},
            			yaxis: {
            				ticks: false
            			},
            			legend: {
	   				        show: false
	   				    },
            			grid: {
            				borderWidth: 0,
            				hoverable: true,
	   				        clickable: true
            			}
            		});
                    elem.show();
                }else{
                    chart.setData(v);
                    chart.setupGrid();
                    chart.draw();
                }
            });
                       
            
            var previousPoint = null; 
            elem.bind("plothover", function(event, pos, obj) {

				if (!obj) {
					$("#tooltip").remove();
					return;
				}
				
				if (previousPoint != obj.datapoint) { 
                    previousPoint = obj.datapoint; 
                    $("#tooltip").remove(); 
                 
					$('<div id="tooltip">' + obj.series.label +'</div>').css( { 
				            position: 'absolute', 
				            display: 'none', 
				            top: pos.pageY + 5, 
				            left: pos.pageX + 5, 
				            border: '1px solid #fdd', 
				            padding: '2px',
				            'background-color': '#fee', 
				            opacity: 0.80 
				        }).appendTo("body").fadeIn(200); 
			    }

			});
			
            
            //elem.show();
        }
    };
});

App.directive('fblike', function() {
    return {
        restrict: 'A',
        scope: true,
        controller: function($scope, $attrs) {
            // Load the SDK Asynchronously
            (function(d){
                var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
                if (d.getElementById(id)) {return;}
                js = d.createElement('script'); js.id = id; js.async = true;
                js.src = "//connect.facebook.net/en_US/all.js";
                ref.parentNode.insertBefore(js, ref);
            }(document));

            (function(d, s, id) {
                var js, fjs = d.getElementsByTagName(s)[0];
                if (d.getElementById(id)) return;
                js = d.createElement(s); js.id = id;
                js.src = "//connect.facebook.net/en_GB/all.js#xfbml=1";
                fjs.parentNode.insertBefore(js, fjs);
            }(document, 'script', 'facebook-jssdk'));

            function login() {
                FB.login(function(response) {
                        if (response.authResponse) {
                            console.log('FB.login connected');
                            fetch();
                        } else {
                            console.log('FB.login cancelled');
                        }
                    }, { scope: 'email,read_stream' }
                );
            };

            function fetch() {
                $http.post('/facebook/fetch', $scope.auth
                    ).success(function(data) {
                        window.location.reload(true);
                        $scope.fetch_status = data.status;
                    }).error(function(data) {
                        console.log('error: '+data);
                        $scope.fetch_status = data.status;
                    });
            }

            $scope.fetch = function() {
                if ($scope.login_status == 'connected') {
                    console.log('fetch');
                    fetch();
                } else {
                    login();
                }
            };
        },
        link: function(scope, element, attrs, controller) {
            // Additional JS functions here
            window.fbAsyncInit = function() {
                FB.init({
                    appId      : attrs.facebook, // App ID
                    channelUrl : '//localhost:3000/channel.html', // Channel File
                    status     : true, // check login status
                    cookie     : true, // enable cookies to allow the server to access the session
                    xfbml      : true  // parse XFBML
                });

                // Additional init code here
                FB.getLoginStatus(function(response) {
                    if (response.status === 'connected') {
                        // connected
                        scope.auth = response.authResponse;
                    } else if (response.status === 'not_authorized') {
                        // not_authorized
                    } else {
                        // not_logged_in
                    }
                    scope.login_status = response.status;
                    scope.$apply();
                });
            }; // end of fbAsyncInit
        }
    }
});
