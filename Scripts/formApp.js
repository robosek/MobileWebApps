angular.module("ngAnimate").controller("ContestFormController", ["$scope", "SendContestData", function($scope, SendContestData){
    $scope.formData = {
        title: "Dlaczego wybieram EB?",
        content: "Chcesz wygrać samochód, tablet lub noworoczny zapas piwa EB? Napisz zabawny wiersz lub piosenkę, w którym powiesz dlaczego wybierasz właśnie EB i podziel się nim z nami! Na zgłoszenia czekamy do 1.02.2016 r.",
        name: "Imię",
        surname: "Nazwisko",
        email: "E-mail",
        phone: "Telefon",
        text: "Twój wiersz",
        dataUseApproval: "Wyrażam zgodę na przetwarzanie moich danych osobowych przez Grupę Żywiec S.A.",
        save: "Wyślij",
        saveInProgress: "Wysyłanie...",
        saveSuccess: "Twoje zgłoszenie zostało wysłane.",
        saveError: "Wystąpił błąd, spróbuj wysłać zgłoszenie ponownie",
        close: "Zamknij",
        textRequired: "Uzupełnienie tekstu jest wymagane",
        nameRequired: "Podanie imienia jest wymagane.",
        surnameRequired: "Podanie nazwiska jest wymagane.",
        emailRequired: "Podanie adresu e-mail jest wymagane.",
        emailFormat: "Nieprawidłowy adres email",
        phoneRequired: "Podanie telefonu jest wymagane.",
        dataUseApprovalRequired: "Wyrażenie zgody jest wymagane"
    };
    $scope.saveBtnText = $scope.formData.save;
    $scope.saveBtnDisabled = false;


    $scope.submit = function(data){
        //override not submitting form implicitly
        $scope.form.$submitted = true;
        if($scope.form.$invalid) return;
        //if ready to send, change send button text and disable it
        $scope.saveBtnText = $scope.formData.saveInProgress;
        $scope.saveBtnDisabled = true;
        SendContestData.sendData(data)
            .success(function(data){

                alert($scope.formData.saveSuccess);
            })
            .error(function(err){
                alert($scope.formData.saveError);

            });
        //restore send button text and enable it
        $scope.saveBtnText = $scope.formData.save;
        $scope.saveBtnDisabled = false;



    };
}]);

angular.module("ngAnimate").factory("SendContestData", ['$http', function($http){
    return {
        //for sending actual data to server
        /*sendData: function(contestData){
            return $http.post("url", contestData)
                .success(function(data){
                    return data;
                })
                .error(function(err){
                    return err;
                });
        }*/
        //temporary test version
        sendData: function(contestData){
            return $http.get("Scripts/version.json")
                .success(function(data){
                    return contestData;
                })
                .error(function(err){
                    return err;
                })
        }
    }

}]);