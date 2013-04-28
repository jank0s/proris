var factories = angular.module('prorisServices', ['ngResource']);
  
  
factories.factory('PB', function($resource){
        return $resource('api/v1/pb/?format=json', {}, {
            query: {method:'GET', isArray:false}
        });
    });
    
factories.factory('BUG', function($resource){
        return $resource('api/v1/bug/?format=json', {}, {
            query: {method:'GET', isArray:false}
        });
    });

factories.factory('PBItem', function($resource){
        return $resource('api/v1/category/?format=json', {}, {
            query: {method:'GET', isArray:false}
        });
    });
    
factories.factory('BUGBu', function($resource){
        return $resource('api/v1/bu/?format=json', {}, {
            query: {method:'GET', isArray:false}
        });
    });
    
factories.factory('BUGBuItem', function($resource){
        return $resource('api/v1/category/?format=json', {}, {
            query: {method:'GET', isArray:false}
        });
    });
