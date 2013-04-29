var factories = angular.module('prorisServices', ['ngResource']);
  
  
factories.factory('PB', function($resource, $routeParams){
        return $resource('pb/:year', {}, {
            query: {method:'GET', params:{year:$routeParams.year}, isArray:false}
        });
    });
    
factories.factory('BUG', function($resource, $routeParams){
        return $resource('api/v1/bug', {}, {
            query: {method:'GET', params:{format:"json", year:$routeParams.year}, isArray:false}
        });
    });

factories.factory('PBItem', function($resource, $routeParams){
        return $resource('api/v1/category', {}, {
            query: {method:'GET', params:{format:"json", year:$routeParams.year, pbid:$routeParams.pbid},isArray:false}
        });
    });
    
factories.factory('BUGBu', function($resource, $routeParams){
        return $resource('api/v1/bu', {}, {
            query: {method:'GET', params:{format:"json", year:$routeParams.year, bugid:$routeParams.bugid}, isArray:false}
        });
    });
    
factories.factory('BUGBuItem', function($resource, $routeParams){
        return $resource('api/v1/category', {}, {
            query: {method:'GET', params:{format:"json", year:$routeParams.year, bugid:$routeParams.bugid, buid:$routeParams.buid}, isArray:false}
        });
    });
