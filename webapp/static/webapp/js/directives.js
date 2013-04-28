App.directive('piechart', function() {
    return {
        restrict: 'EA',
        link: function(scope, elem, attrs) {
            var data = scope[attrs.ngModel];
            $.plot(elem, data, {
		           series: {
				        pie: {
				            show: true,
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
        }
    };
});