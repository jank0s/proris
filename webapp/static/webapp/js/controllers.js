function PBCtrl($scope, $routeParams, $http) {
   
    $http.get('pb/' + $routeParams.year).success(function(data) {
        $scope.its = data;  
        
        var datapie = [];
        var count = 0;
        for (var i = 0; i < 15; i++) {
        	if(i < data.list.length){
        		if(data.list[i].percent < 1)
        			break;
        		
        		var temp = {};
    	    	temp.label = data.list[i].name;
    	    	temp.data = data.list[i].percent;
    	    	datapie.push(temp);
    	    	
    	    	count += data.list[i].percent;
        	}
		}
	    
        var temp = {};
        temp.label = "Ostali";
        temp.data = 100 - count;
        datapie.push(temp);
        
	    $scope.pie = datapie;
    });

    $http.get('year/').success(function(data) {
        $scope.yList = data;
    });
   
	$scope.pie = null;
    $scope.year = $routeParams.year;
}

function BUGCtrl($scope, $routeParams, $http) {

	$http.get('bug/' + $routeParams.year).success(function(data) {
        $scope.its = data;
        
        var datapie = [];
        var count = 0;
        for (var i = 0; i < 15; i++) {
        	if(i < data.list.length){
        		if(data.list[i].percent < 1)
        			break;
        		        		
        		var temp = {};
    	    	temp.label = data.list[i].name;
    	    	temp.data = data.list[i].percent;
    	    	datapie.push(temp);
    	    	
    	    	count += data.list[i].percent;
        	}
		}
	    
        var temp = {};
        temp.label = "Ostali";
        temp.data = 100 - count;
        datapie.push(temp);
        
        $scope.pie = datapie;
        
    });

    $http.get('year/').success(function(data) {
        $scope.yList = data;
    });
    

	$scope.pie = null; 
	$scope.year = $routeParams.year;
}

function PBItemCtrl($scope, $routeParams, $http) {

	$http.get('pb/' + $routeParams.year + '/' + $routeParams.pbid).success(function(data) {
        $scope.its = data;
        
        var datapie = [];
        var count = 0;
        for (var i = 0; i < 15; i++) {
        	if(i < data.list.length){
        		if(data.list[i].percent < 1)
        			break;
        		        		
        		var temp = {};
    	    	temp.label = data.list[i].name;
    	    	temp.data = data.list[i].percent;
    	    	datapie.push(temp);
    	    	
    	    	count += data.list[i].percent;
        	}
		}
	    
        var temp = {};
        temp.label = "Ostali";
        temp.data = 100 - count;
        datapie.push(temp);
	    
	    $scope.pie = datapie;
    });

    $http.get('year/').success(function(data) {
        $scope.yList = data;
    });
    
	$scope.pie = null;
    $scope.year = $routeParams.year;
    $scope.pbid = $routeParams.pbid;
}

function BUGBuCtrl($scope, $routeParams, $http) {

	$http.get('bug/' + $routeParams.year + '/' + $routeParams.bugid).success(function(data) {
        $scope.its = data;
        
        var datapie = [];
        var count = 0;
        for (var i = 0; i < 15; i++) {
        	if(i < data.list.length){
        		if(data.list[i].percent < 1)
        			break;
        		        		
        		var temp = {};
    	    	temp.label = data.list[i].name;
    	    	temp.data = data.list[i].percent;
    	    	datapie.push(temp);
    	    	
    	    	count += data.list[i].percent;
        	}
		}
	    
        var temp = {};
        temp.label = "Ostali";
        temp.data = 100 - count;
        datapie.push(temp);
	    
	    $scope.pie = datapie;
    });

    $http.get('year/').success(function(data) {
        $scope.yList = data;
    });
    
    $scope.pie = null;
	$scope.year = $routeParams.year;
	$scope.bugid = $routeParams.bugid;
}

function BUGBuItemCtrl($scope, $routeParams, $http) {

	$http.get('bug/' + $routeParams.year + '/' + $routeParams.bugid + '/' + $routeParams.buid).success(function(data) {
        $scope.its = data;
        
        var datapie = [];
        var count = 0;
        for (var i = 0; i < 15; i++) {
        	if(i < data.list.length){
        		if(data.list[i].percent < 1)
        			break;
        		
        		var temp = {};
    	    	temp.label = data.list[i].name;
    	    	temp.data = data.list[i].percent;
    	    	datapie.push(temp);
    	    	
    	    	count += data.list[i].percent;
        	}
		}
	    
        var temp = {};
        temp.label = "Ostali";
        temp.data = 100 - count;
        datapie.push(temp);
        
	    $scope.pie = datapie;
    });

    $http.get('year/').success(function(data) {
        $scope.yList = data;
    });
    
    $scope.pie = null;
    $scope.year = $routeParams.year;
    $scope.bugid = $routeParams.bugid;
    $scope.buid = $routeParams.buid;
}