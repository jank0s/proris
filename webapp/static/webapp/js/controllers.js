function PBCtrl($scope, $routeParams, $http) {
   
    $http.get('pb/' + $routeParams.year).success(function(data) {
        $scope.its = data;  
        
        var datapie = [];
        var count = 0;
        for (var i = 0; i < 15; i++) {
        	if(i < data.list.length){
        		if(data.list[i].percent < 2)
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
        		if(data.list[i].percent < 2)
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
        		if(data.list[i].percent < 2)
        			break;
        		        		
        		var temp = {};
    	    	temp.label = data.list[i].name + " - " + (Math.round(data.list[i].percent * 10) / 10) + " %";
    	    	temp.data = data.list[i].percent;
    	    	datapie.push(temp);
    	    	
    	    	count += data.list[i].percent;
        	}
		}
	    
        var temp = {};
        temp.label = "Ostali - " + (Math.round((100 - count) * 10) / 10) + " %";
        temp.data = 100 - count;
        datapie.push(temp);
        
        var databar = [];
        for (var i = 0; i < data.ref.length; i++){
        	
        	var temp = {};
        	
        	if (data.ref[i].year == $routeParams.year)
        		temp.color = "#BED4E2";
        	else
        		temp.color = "#E9BD5E";
        	
        	var tempData = [];
        	tempData.push(data.ref[i].year);
        	tempData.push(data.ref[i].value);
        	temp.data = [ tempData ];
        	temp.label = Math.round(data.ref[i].value).formatMoney(0, "") + " €";
        	
        	databar.push(temp);
        }
	    
	    $scope.pie = datapie;
	    $scope.bar =  databar;
	});

    $http.get('year/').success(function(data) {
        $scope.yList = data;
    });
    
	$scope.pie = null;
	$scope.bar = null;
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
        		if(data.list[i].percent < 2)
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
        		if(data.list[i].percent < 2)
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