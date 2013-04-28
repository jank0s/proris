angular.module('proris', []).
    config(['$routeProvider', function($routeProvider) {
        $routeProvider.
            when('/pb/:year', {templateUrl: 'static/webapp/templates/view.html',   controller: PBCtrl}).
            when('/', {templateUrl: 'static/webapp/templates/index.html'}).
            otherwise({redirectTo: '/'});
    }]);
