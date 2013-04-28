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

function BUGBuCtrl($scope, BUGBu) {
	$scope.its = BUGBu.query();
}