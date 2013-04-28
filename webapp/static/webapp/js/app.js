angular.module('proris', ['prorisServices']).
    config(['$routeProvider', function($routeProvider) {
        $routeProvider.
            when('/pb/:year/:pbid', {templateUrl: 'static/webapp/templates/pb_item.html',   controller: PBItemCtrl}).
            when('/pb/:year', {templateUrl: 'static/webapp/templates/pb.html',   controller: PBCtrl}).
            when('/bug/:year', {templateUrl: 'static/webapp/templates/bug.html',   controller: BUGCtrl}).
            when('/', {templateUrl: 'static/webapp/templates/index.html'}).
            otherwise({redirectTo: '/'});
    }]);
