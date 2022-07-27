function mOnboardingScreen(mShow) {
    var x = document.getElementById("onBoardingScreen");
    if (mShow == false) {
      x.style.display = "none";
    }
  }

  function mDocumentationScreen(mShow) {
    var x = document.getElementById("mDocumentationScreen");
    if (mShow == false) {
      x.style.display = "block";
    }
  }

function mGetstarted(){
    const mShowOnBoardingScreen = false;
    mOnboardingScreen(mShowOnBoardingScreen)
    mDocumentationScreen(mShowOnBoardingScreen)

}
