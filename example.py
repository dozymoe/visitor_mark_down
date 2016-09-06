try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup

from visitor_mark_down import intrude
from visitor_mark_down.affiliation.beautifulsoup import Door2DoorSoup

doc = BeautifulSoup("""
<body dir="ltr">
    <!-- Contains an alternate page title set on page init for cert errors. -->
    <div id="certErrorPageTitle" style="display: none;">Insecure Connection</div>

    <!-- ERROR ITEM CONTAINER (removed during loading to avoid bug 39098) -->
    

    <!-- PAGE CONTAINER (for styling purposes only) -->
    <div id="errorPageContainer" class="container">

      <!-- Error Title -->
      <div class="title">
        <h1 class="title-text">Server not found</h1>
      </div>

      <!-- LONG CONTENT (the section most likely to require scrolling) -->
      <div id="errorLongContent">

        <!-- Short Description -->
        <div id="errorShortDesc">
          <p id="errorShortDescText">Firefox can't find the server at gitter.im.</p>
        </div>
        <p hidden="true" id="badStsCertExplanation">This site uses HTTP
Strict Transport Security (HSTS) to specify that Firefox only connect
to it securely. As a result, it is not possible to add an exception for this
certificate.</p>

        <!-- Long Description (Note: See netError.dtd for used XHTML tags) -->
        <div id="errorLongDesc">
<ul xmlns="http://www.w3.org/1999/xhtml"> 
  <li>Check the address for typing errors such as 
    <strong>ww</strong>.example.com instead of 
    <strong>www</strong>.example.com</li> 
  <li>If you are unable to load any pages, check your computer's network 
    connection.</li> 
  <li>If your computer or network is protected by a firewall or proxy, make sure
    that Firefox is permitted to access the Web.</li> 
</ul>
</div>

        <div id="learnMoreContainer">
          <p><a href="https://support.mozilla.org/kb/what-does-your-connection-is-not-secure-mean" id="learnMoreLink" target="new">Learn more…</a></p>
        </div>

        <div id="certErrorButtonContainer" class="button-container">
          <button id="returnButton" class="primary" autocomplete="off" autofocus="true">Go Back</button>
          <div class="button-spacer"></div>
          <button id="advancedButton" autocomplete="off" autofocus="true">Advanced</button>
        </div>
      </div>

      <div id="netErrorButtonContainer" class="button-container">
        
      <button id="errorTryAgain" class="primary" autocomplete="off" onclick="retryThis(this);" autofocus="true">Try Again</button></div>

      <script>
        // Only do autofocus if we're the toplevel frame; otherwise we
        // don't want to call attention to ourselves!  The key part is
        // that autofocus happens on insertion into the tree, so we
        // can remove the button, add @autofocus, and reinsert the
        // button.
        if (window.top == window) {
            var button = document.getElementById("errorTryAgain");
            var parent = button.parentNode;
            button.remove();
            button.setAttribute("autofocus", "true");
            parent.appendChild(button);
        }
      </script>

      <!-- UI for option to report certificate errors to Mozilla. Removed on
           init for other error types .-->
      <div id="certificateErrorReporting">
        <p>
          <input type="checkbox" id="automaticallyReportInFuture"/>
          <label for="automaticallyReportInFuture" id="automaticallyReportInFuture">Report errors like this to help Mozilla identify and block malicious sites</label>
        </p>
      </div>

      <div id="advancedPanelContainer">
        <div id="weakCryptoAdvancedPanel" class="advanced-panel">
          <div id="weakCryptoAdvancedDescription">
            <p><span class="hostname"></span> uses security technology that is outdated and vulnerable to attack. An attacker could easily reveal information which you thought to be safe.</p>
          </div>
          <div id="advancedLongDesc"></div>
          <div id="overrideWeakCryptoPanel">
            <a id="overrideWeakCrypto" href="#">(Not secure) Try loading <span class="hostname"></span> using outdated security</a>
          </div>
        </div>

        <div id="badCertAdvancedPanel" class="advanced-panel">
          <p id="badCertTechnicalInfo"></p>
          <button id="exceptionDialogButton">Add Exception…</button>
        </div>
      </div>

    </div>

    <div id="certificateErrorDebugInformation">
      <a name="technicalInformation"></a>
      <button id="copyToClipboard">Copy text to clipboard</button>
      <div id="certificateErrorText"></div>
      <button id="copyToClipboard">Copy text to clipboard</button>
    </div>

    <!--
    - Note: It is important to run the script this way, instead of using
    - an onload handler. This is because error pages are loaded as
    - LOAD_BACKGROUND, which means that onload handlers will not be executed.
    -->
    <script type="application/javascript">initPage();</script>

  </body>
""")

print(''.join(intrude(doc, offer=Door2DoorSoup)))
