var App = angular.module('proris', []);

App.config(['$routeProvider', function($routeProvider) {
        $routeProvider.
            when('/pb/:year/:pbid', {templateUrl: 'static/webapp/templates/pb_item.html',   controller: PBItemCtrl}).
            when('/pb/:year', {templateUrl: 'static/webapp/templates/pb.html',   controller: PBCtrl}).
            when('/bug/:year/:bugid/:buid', {templateUrl: 'static/webapp/templates/bug_bu_item.html',   controller: BUGBuItemCtrl}).
            when('/bug/:year/:bugid', {templateUrl: 'static/webapp/templates/bug_bu.html',   controller: BUGBuCtrl}).
            when('/bug/:year', {templateUrl: 'static/webapp/templates/bug.html',   controller: BUGCtrl}).
            when('/', {templateUrl: 'static/webapp/templates/index.html'}).
            otherwise({redirectTo: '/'});
    }]);