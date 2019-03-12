var botPart1 = '<div class="chat-container darker"><img src="../static/Assets/avatar.jpg" alt="Avatar" style="width:100%;"><p>';
var userPart1 = '<div class="chat-container"><img src="../static/Assets/userImage.png" alt="Avatar" style="width:100%;" class = "right"><p>'
var botPart3 ='</p></div>';

var isLoggedIn = false;

function toggleLoginModal()
{
    if($(".modal").css("display") == "none")
    {
        $(".modal").css("display", "block");
    }
    else
    {
        $(".modal").css("display", "none");
    }
}

//Bot Window pop up...
function openBotWindow()
{    
    $("#botWindow").css("display", "block");
    snackbar("Launching Bot Deku !")
    console.log("works !")
}

function closeBotWindow()
{
    $("#botWindow").css("display", "none");
}

//User Message Reciever...
function sendMessage()
{
    var utext = $("#msgBox").val();
    var flag = false;
    $(".chat-parent-container").append(userPart1 + utext + botPart3);
    $.ajax({
        type: "POST",
        url: "/botresponse",
        data: {'utext' : utext},
        success: function (response) {
            console.log(botPart1 + response + botPart3);
            $(".chat-parent-container").append(botPart1 + response + botPart3);
            flag = true;
        },
        error: function(){
            $(".chat-parent-container").append(botPart1 + "Sorry, Technical Issues !" + botPart3);
        },
        complete: function(){
            $("#msgBox").val('').empty();
        }
    });        
    
}

/*      Snack bar function      */
function snackbar(message , color = "green") {

    var green_background = "rgb(139, 182, 121)";
    var red_background = "rgb(163, 91, 101)";

    var red_text = "rgb(122, 34, 47)"
    var green_text = "rgb(55, 131, 54)"

    if(color == "green")
    {
        $("#snackbar").css("background-color", green_background);
        $("#snackbar").css("color", green_text);
    }
    else
    {
        $("#snackbar").css("background-color", red_background);
        $("#snackbar").css("color", red_text);
    }


    $("#snackbar").text(message);    
    $("#snackbar").addClass("show");
    
    setTimeout(function name(params) {
        $("#snackbar").removeClass("show");
    }, 3000);
}
/* Snackbar end */



/*      Login function       */
function login()
{
    $.ajax({
        type: "POST",
        url: "/login",
        data: $("#LoginForm").serialize(),
        success: function (response) {
            console.log(response);
            CloseModal();
            if(response['flag'] == 1)
            {
                snackbar("Login Successfull !" , "green");
                loggedIn(response);
            }
            else    
                snackbar("Login Failed !" , "red");            
        },
        error: function () {
            snackbar("Login Failed !" , "red");
        }
    });
}

/*      Signup Function      */
function signup()
{
    $.ajax({
        type: "POST",
        url: "/signup",
        data: $("#SignupForm").serialize(),
        success: function (response) {
            console.log(response);
            CloseModal();
            snackbar("Signup Successfull !" , "green");
            loggedIn(response);
        },
        error: function () {
            snackbar("Signup Failed !" , "red");
        }
    });
}

/*      Modal Close      */
function CloseModal() {
    $(".modal").css("display", "none");
}





/*      Document Ready Functions     */
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

//Login Modal...

$("#loginButton").click(function (e) {
    $(".modal").css("display", "block");
    $("#SignUpModal").css("z-index", "0");
    $("#LoginModal").css("z-index", "8");
    e.preventDefault();
});

$(".close").click(function (e) {
    CloseModal();
    e.preventDefault();
});

});
