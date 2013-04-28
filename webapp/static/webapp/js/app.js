angular.module('proris', ['prorisServices']).
    config(['$routeProvider', function($routeProvider) {
        $routeProvider.
            when('/pb/:year', {templateUrl: 'static/webapp/templates/view.html',   controller: PBCtrl}).
            when('/bug/:year', {templateUrl: 'static/webapp/templates/view.html',   controller: BUGCtrl}).
            when('/', {templateUrl: 'static/webapp/templates/index.html'}).
            otherwise({redirectTo: '/'});
    }]);
