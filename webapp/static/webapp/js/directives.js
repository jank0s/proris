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