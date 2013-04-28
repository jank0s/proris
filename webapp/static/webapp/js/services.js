angular.module('prorisServices', ['ngResource'])
    .factory('PB', function($resource){
        return $resource('api/v1/pb/?format=json', {}, {
            query: {method:'GET', isArray:false}
        });
    });
