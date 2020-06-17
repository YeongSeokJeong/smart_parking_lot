
function getUiConfig() {
  return {
    'callbacks': {
      'signInSuccessWithAuthResult': function(authResult) {
        if (authResult.user) {
          handleSignedInUser(authResult.user);
        }
        if (authResult.additionalUserInfo) {
          document.getElementById('is-new-user').textContent =
              authResult.additionalUserInfo.isNewUser ?
              'New User' : 'Existing User';
        }
        return false;
      }
    },

    'signInFlow': 'popup',
    'signInOptions': [
      
      {
        provider: firebase.auth.GoogleAuthProvider.PROVIDER_ID,
        authMethod: 'https://accounts.google.com',
        clientId: CLIENT_ID
      },
      {
        provider: firebase.auth.FacebookAuthProvider.PROVIDER_ID,
        scopes :[
          'public_profile',
          'email',
          'user_likes',
          'user_friends'
        ]
      },
      {
        provider: firebase.auth.EmailAuthProvider.PROVIDER_ID,
        requireDisplayName: true,
        signInMethod: getEmailSignInMethod()
      },
      {
        provider: firebase.auth.PhoneAuthProvider.PROVIDER_ID,
        recaptchaParameters: {
          size: getRecaptchaMode()
        }
      },
      {
        provider: 'microsoft.com',
        loginHintKey: 'login_hint'
      },
      {
        provider: 'apple.com',
      },
      firebaseui.auth.AnonymousAuthProvider.PROVIDER_ID
    ],
    
    'tosUrl': 'https://accounts.google.com',
    'privacyPolicyUrl': 'https://accounts.google.com',
    'credentialHelper': CLIENT_ID && CLIENT_ID != 'YOUR_OAUTH_CLIENT_ID' ?
        firebaseui.auth.CredentialHelper.GOOGLE_YOLO :
        firebaseui.auth.CredentialHelper.ACCOUNT_CHOOSER_COM
  };
}

var ui = new firebaseui.auth.AuthUI(firebase.auth());
ui.disableAutoSignIn();


/**
 * @return {string} The URL of the FirebaseUI standalone widget.
 */
function getWidgetUrl() {
  return '/widget#recaptcha=' + getRecaptchaMode() + '&emailSignInMethod=' +
      getEmailSignInMethod();
}

//데이터베이스에 연결
const preObject = document.getElementById('object');

const dbRefObject = firebase.database().ref().child('object');  //child 호출, child키 생성

//데이터 동기화
dbRefObject.on('value', snap => console.log(snap.val()));

dbRefObject.on('value', snap => 
  preObject.innerText = JSON.stringify(snap.val(), null, 3));

dbRefObject.on('child_changed', snap =>{
  const liChanged = document.createElementById(snap.key);
  liChanged.innerText = snap.val()
  
});
dbRefObject.on('child_removed', snap =>{
  liChanged.innerText = snap.val()
  
});
//테이블 연결
var rootRef = firebase.database().ref();
    
    var ref = rootRef.child('object/guestData');
    var ref2 = rootRef.child('object/carData');    

    ref.orderByChild("date").startAt(3).on('value', function(snap) { 
    console.log(snap.key)
    document.getElementById("answer").innerHTML = "";
        
    snap.forEach(function(child){
    var childData = child.val();
    var carNum = childData.carNum;
    var date = childData.date;
    var time = childData.time;
    
    
    document.getElementById("answer").innerHTML += "<tr><td ></td><td>" + carNum + "</td><td> " + time + "</td><td>" + "</td><td>" + date + "</td></tr>";            
    });
});  

/**
 * 사용자 로그인시 출력화면 
 * @param {!firebase.User} user
 */
var handleSignedInUser = function(user) {
  document.getElementById('user-signed-in').style.display = 'block';
  document.getElementById('user-signed-out').style.display = 'none';
  document.getElementById('name').textContent = user.displayName;
  document.getElementById('email').textContent = user.email;
  document.getElementById('phone').textContent = user.phoneNumber;

  if (user.photoURL) {
    var photoURL = user.photoURL;
    if ((photoURL.indexOf('googleusercontent.com') != -1) ||
        (photoURL.indexOf('ggpht.com') != -1)) {
      photoURL = photoURL + '?sz=' +
          document.getElementById('photo').clientHeight;
    }
    document.getElementById('photo').src = photoURL;
    document.getElementById('photo').style.display = 'block';
  } else {
    document.getElementById('photo').style.display = 'none';
  }
};

var handleSignedOutUser = function() {
  document.getElementById('user-signed-in').style.display = 'none';
  document.getElementById('user-signed-out').style.display = 'block';
  ui.start('#firebaseui-container', getUiConfig());
};

firebase.auth().onAuthStateChanged(function(user) {
  document.getElementById('loading').style.display = 'none';
  document.getElementById('loaded').style.display = 'block';
  user ? handleSignedInUser(user) : handleSignedOutUser();
});

function handleConfigChange() {
  var newRecaptchaValue = document.querySelector(
      'input[name="recaptcha"]:checked').value;
  var newEmailSignInMethodValue = document.querySelector(
      'input[name="emailSignInMethod"]:checked').value;
  location.replace(
      location.pathname + '#recaptcha=' + newRecaptchaValue +
      '&emailSignInMethod=' + newEmailSignInMethodValue);
  ui.reset();
  ui.start('#firebaseui-container', getUiConfig());
}

var initApp = function() {
  document.getElementById('sign-out').addEventListener('click', function() {
    firebase.auth().signOut();
  });

  document.getElementById('recaptcha-normal').addEventListener(
      'change', handleConfigChange);
  document.getElementById('recaptcha-invisible').addEventListener(
      'change', handleConfigChange);
  
  document.querySelector(
      'input[name="recaptcha"][value="' + getRecaptchaMode() + '"]')
      .checked = true;

  document.getElementById('email-signInMethod-password').addEventListener(
      'change', handleConfigChange);
  document.getElementById('email-signInMethod-emailLink').addEventListener(
      'change', handleConfigChange);

  document.querySelector(
      'input[name="emailSignInMethod"][value="' + getEmailSignInMethod() + '"]')
      .checked = true;
};

window.addEventListener('load', initApp);
