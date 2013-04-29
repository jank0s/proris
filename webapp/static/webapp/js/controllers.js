function PBCtrl($scope, $routeParams, PB) {
    $scope.its = PB.query();
    $scope.year = $routeParams.year;
}

function BUGCtrl($scope, $routeParams, BUG) {
	$scope.its = BUG.query();
	$scope.year = $routeParams.year;
}

function PBItemCtrl($scope, PBItem) {
	$scope.its = PBItem.query();
}

function BUGBuCtrl($scope, $routeParams, BUGBu) {
	$scope.its = BUGBu.query();
	$scope.year = $routeParams.year;
	$scope.bugid = $routeParams.bugid;
}

function BUGBuItemCtrl($scope, BUGBuItem) {
	$scope.its = BUGBuItem.query();
}

function PBPieCtrl($scope){
    
    var data1 = [
			{ label: "Series1",  data: 10},
			{ label: "Series2",  data: 30},
			{ label: "Series3",  data: 90},
			{ label: "Series4",  data: 70},
			{ label: "Series5",  data: 80},
			{ label: "Series6",  data: 110}
		];
    
    $scope.data = data1;
}

function PBItemPieCtrl($scope){
    
    var data1 = [
			{ label: "Series1",  data: 110},
			{ label: "Series2",  data: 80},
			{ label: "Series3",  data: 70},
			{ label: "Series4",  data: 90},
			{ label: "Series5",  data: 30},
			{ label: "Series6",  data: 10}
		];
    
    $scope.data = data1;
}

function BUGPieCtrl($scope){
    
    var data1 = [
			{ label: "Series1",  data: 13},
			{ label: "Series2",  data: 50},
			{ label: "Series3",  data: 42},
			{ label: "Series4",  data: 70},
			{ label: "Series5",  data: 20},
			{ label: "Series6",  data: 74}
		];
    
    $scope.data = data1;
}

function BUGBuPieCtrl($scope){
    
    var data1 = [
			{ label: "Series1",  data: 10},
			{ label: "Series2",  data: 30},
			{ label: "Series3",  data: 90},
			{ label: "Series4",  data: 70},
			{ label: "Series5",  data: 80},
			{ label: "Series6",  data: 110}
		];
    
    $scope.data = data1;
}

function BUGBuItemPieCtrl($scope){
    
    var data1 = [
			{ label: "Series1",  data: 74},
			{ label: "Series2",  data: 75},
			{ label: "Series3",  data: 33},
			{ label: "Series4",  data: 43},
			{ label: "Series5",  data: 80},
			{ label: "Series6",  data: 200}
		];
    
    $scope.data = data1;
}