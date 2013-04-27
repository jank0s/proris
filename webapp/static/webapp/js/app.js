angular.module('proris', []).
    config(['$routeProvider', function($routeProvider) {
        $routeProvider.
            when('/', {templateUrl: 'static/webapp/templates/index.html',   controller: BudgetCtrl}).
            otherwise({redirectTo: '/'});
    }]);
