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