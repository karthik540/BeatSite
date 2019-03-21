var botPart1 = '<div class="chat-container darker"><img src="../static/Assets/avatar.jpg" alt="Avatar" style="width:100%;"><p>';
var userPart1 = '<div class="chat-container"><img src="../static/Assets/userImage.png" alt="Avatar" style="width:100%;" class = "right"><p>'
var botPart3 ='</p></div>';

var player;
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
            //console.log(botPart1 + response[1] + botPart3);
            $(".chat-parent-container").append(botPart1 + response['response'] + botPart3);
            flag = true;
            bot_Event_Handler(utext , response['class']);
        },
        error: function(){
            $(".chat-parent-container").append(botPart1 + "Sorry, Technical Issues !" + botPart3);
        },
        complete: function(){
            $("#msgBox").val('').empty();
        }
    });        
    
}

/*      Bot Event handler function      */

function bot_Event_Handler(user_request , intent_class) {
    
    if(intent_class == "Browse")
        window.location="http://127.0.0.1:5000/browse/";

    //console.log(bot_response);
    if(intent_class == "pause song")
        pauseVideo();
    
    if(intent_class == "start song")
        playVideo();

    if(intent_class == "mute song")
        muteVideo();
    
    if(intent_class == "unmute song")
        unmuteVideo();
    
    if(intent_class == "increase volume")
        increaseVolume();

    if(intent_class == "decrease volume")
        decreaseVolume();  
    
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

function loggedIn(user_data)
{   
    $("#editButton").show();
    $("#editButton").html("<i class='fa fa-fw fa-user editButton'></i>" + user_data['name']);
    //$("#editButton").text( "<i class='fa fa-fw fa-user editButton'></i>" + user_data['name']);
    $("#loginButton").hide();
    $("#signUpButton").hide();
}

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

/*      Youtube video Fetcher       */

function getVideoID(songname){
    console.log(songname);

    $.ajax({
        type: "POST",
        url: "/videoId/" + songname,
        success: function (response) {
            console.log(response);
            $("#video_container").css("padding", "3% 25%");
            $("#video_container").html("<iframe id='player' width='100%' height='400px' src='https://www.youtube.com/embed/" + response + "?autoplay=1&enablejsapi=1&html5=1' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen=''></iframe>");
            onYouTubePlayerAPIReady();
        }
    });
}

/*      Youtube Video Controller    */

var player;
function onYouTubePlayerAPIReady() {
    // global player
    
    //console.log("object created!");
    player = new YT.Player('player', {
        events: {
        
        }
});
}


function playVideo(){
    player.playVideo();
}

function pauseVideo(){
    player.pauseVideo();
}

function muteVideo() {
    player.mute();
}

function unmuteVideo() {
    player.unmute();
}

function increaseVolume() {
    if(player.isMuted())
        unmuteVideo();
    player.setVolume(player.getVolume() + 10);
}

function decreaseVolume() {
    player.setVolume(player.getVolume() - 10);
}


/*      Document Ready Functions     */
$(document).ready(function () {
/*
// global player
function onYouTubePlayerAPIReady() {
    player = new YT.Player(document.querySelector('iframe'), {});
}

// Inject YouTube API script
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/player_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
*/
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
