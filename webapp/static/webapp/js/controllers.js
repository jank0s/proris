function PBCtrl($scope, $routeParams, $http) {
   
    $http.get('pb/' + $routeParams.year).success(function(data) {
        $scope.its = data;  
    });

    $http.get('year/').success(function(data) {
        $scope.yList = data;
    });
   
    var datapie = [];
    
    for (var i = 0; i < 10; i++) {
	    	var temp = {};
	    	temp.label = "Placeholder";
	    	temp.data = Math.random();
	    	datapie.push(temp);
	}
    
	$scope.pie = datapie;
    $scope.year = $routeParams.year;
}

function BUGCtrl($scope, $routeParams, $http) {

	$http.get('bug/' + $routeParams.year).success(function(data) {
        $scope.its = data;
    });

    $http.get('year/').success(function(data) {
        $scope.yList = data;
    });
    
    var datapie = [];
    
    for (var i = 0; i < 10; i++) {
	    	var temp = {};
	    	temp.label = "Placeholder";
	    	temp.data = Math.random();
	    	datapie.push(temp);
	}
    
	$scope.pie = datapie;
    
	$scope.year = $routeParams.year;
}

function PBItemCtrl($scope, $routeParams, $http) {

	$http.get('pb/' + $routeParams.year + '/' + $routeParams.pbid).success(function(data) {
        $scope.its = data;
    });

    $http.get('year/').success(function(data) {
        $scope.yList = data;
    });
    
    var datapie = [];
    
    for (var i = 0; i < 10; i++) {
	    	var temp = {};
	    	temp.label = "Placeholder";
	    	temp.data = Math.random();
	    	datapie.push(temp);
	}
    
	$scope.pie = datapie;
    $scope.year = $routeParams.year;
    $scope.pbid = $routeParams.pbid;
}

function BUGBuCtrl($scope, $routeParams, $http) {

	$http.get('bug/' + $routeParams.year + '/' + $routeParams.bugid).success(function(data) {
        $scope.its = data;
    });

    $http.get('year/').success(function(data) {
        $scope.yList = data;
    });
    
    var datapie = [];
    
    for (var i = 0; i < 10; i++) {
	    	var temp = {};
	    	temp.label = "Placeholder";
	    	temp.data = Math.random();
	    	datapie.push(temp);
	}
    
	$scope.pie = datapie;
	
	$scope.year = $routeParams.year;
	$scope.bugid = $routeParams.bugid;
}

function BUGBuItemCtrl($scope, $routeParams, $http) {

	$http.get('bug/' + $routeParams.year + '/' + $routeParams.bugid + '/' + $routeParams.buid).success(function(data) {
        $scope.its = data;
    });

    $http.get('year/').success(function(data) {
        $scope.yList = data;
    });
    
    var datapie = [];
    
    for (var i = 0; i < 10; i++) {
	    	var temp = {};
	    	temp.label = "Placeholder";
	    	temp.data = Math.random();
	    	datapie.push(temp);
	}
    
	$scope.pie = datapie;
    $scope.year = $routeParams.year;
    $scope.bugid = $routeParams.bugid;
    $scope.buid = $routeParams.buid;
}