function PBCtrl($scope, $routeParams, PB) {
    $scope.its = PB.query();
    $scope.year = $routeParams.year;
}

function BUGCtrl($scope, BUG) {
	$scope.its = BUG.query();
}

function PBItemCtrl($scope, PBItem) {
	$scope.its = PBItem.query();
}