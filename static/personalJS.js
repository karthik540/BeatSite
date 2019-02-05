function toggleLoginModal(){
    if($(".modal").css("display") == "none")
    {
        $(".modal").css("display", "block");
    }
    else
    {
        $(".modal").css("display", "none");
    }
}


$(document).ready(function () {

//Responsive navbar...
    
$(".icon").click(function (e) { 
    if($(".top-nav").hasClass(".responsive"))
    {
        $(".top-nav").removeClass(".responsive");
                
        console.log("response removed !");
    }
    else
    {
        $(".top-nav").addClass(".responsive");  
        console.log("response added !");
    }
});

//Login and SignUp Modals...

//Signup Modal...
$("#signUpButton").click(function (e) { 
    $(".modal").css("display", "block");
    $("#SignUpModal").css("z-index", "8");
    $("#LoginModal").css("z-index", "0");
    e.preventDefault();
});

//SignUp Modal...
$("#loginButton").click(function (e) { 
    $(".modal").css("display", "block");
    $("#SignUpModal").css("z-index", "0");
    $("#LoginModal").css("z-index", "8");
    e.preventDefault();
});

$(".close").click(function (e) { 
    $(".modal").css("display", "none");
    e.preventDefault();
});

});