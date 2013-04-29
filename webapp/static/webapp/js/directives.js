App.directive('piechart', function() {
    return {
        restrict: 'EA',
        link: function(scope, elem, attrs) {
            var data = scope[attrs.ngModel];
            var chart = null;
                        
            $.plot(elem, data , {
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
			
            
            elem.show();
        }
    };
});