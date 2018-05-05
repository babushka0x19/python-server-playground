
from django.http import HttpResponse

import json


response_data = {}
response_data['result'] = 'error'
response_data['message'] = 'Some error message'



def index(request):
    return HttpResponse("<br>hhhehe</br>")


def say_hi(request):
    return HttpResponse("hi guys")


def error(request):
    from django.http import JsonResponse
    return JsonResponse({'results': 'There was an error, please try again'})


def nice_page(req):
    text = """
    
<!DOCTYPE html>

<!--
Copyright 2017 Google Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

<html lang="en">

<head>

  <!-- Global site tag (gtag.js) - Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=UA-33848682-1"></script>
  <script>
    window.dataLayer = window.dataLayer || [];

    function gtag() {
      window.dataLayer.push(arguments);
    }
    gtag('js', new Date());
    gtag('config', 'UA-33848682-1');
  </script>

  <meta charset="utf-8">
  <meta name="description" content="Simplest possible examples of HTML, CSS and JavaScript.">
  <meta name="author" content="https://samdutton.com">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta itemprop="name" content="simpl.info: simplest possible examples of HTML, CSS and JavaScript">
  <meta itemprop="image" content="images/icons/icon192.png">
  <meta id="theme-color" name="theme-color" content="#fff">

  <title>simpl.info</title>

  <link rel="canonical" href="https://simpl.info">
  <link rel="manifest" href="manifest.json">

  <link rel="apple-touch-icon" href="images/icons/icon180.png">
  <link rel="icon" sizes="32x32" href="images/icons/icon32.png">
  <link rel="icon" sizes="192x192" href="images/icons/icon192.png">
  <link rel="icon" sizes="256x256" href="images/icons/icon256.png">
  <link rel="shortcut icon" href="images/icons/icon72.png">
  <link rel="icon" href="/favicon.ico" type="image/x-icon" />
  <link rel="icon" href="/favicon.ico" type="image/png" />

  <style>
    a {
      color: #15c;
      font-weight: 300;
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }

    a#twitter {
      color: black;
      display: block;
      text-decoration: none;
    }

    a#viewSource {
      border-top: 1px solid #999;
      display: block;
      margin: 1.3em 0 0 0;
      padding: 1em 0 0 0;
    }

    a#twitter div {
      display: inline-block;
      font-weight: 500;
      position: relative;
      top: -13px;
    }

    a#twitter div:hover {
      color: #1da1f2;
    }

    div#links a {
      display: block;
      line-height: 1.3em;
      margin: 0 0 1.5em 0;
    }

    @media (min-width: 1000px) {
      /* hack! to target non-touch devices */
      div#links a {
        line-height: 0.8em;
      }
    }

    body {
      font-family: sans-serif;
      font-weight: 300;
      margin: 0;
      padding: 1em;
      word-break: break-word;
    }

    div#container {
      margin: 0 auto 0 auto;
      max-width: 40em;
      padding: 1em 1.5em 1.3em 1.5em;
    }

    div#highlight {
      background-color: #eee;
      font-size: 1.2em;
      margin: 0 0 50px 0;
      padding: 0.5em 2em;
    }

    div#links {
      padding: 0.5em 0 0 0;
    }

    h1 {
      border-bottom: 1px solid #ccc;
      font-family: sans-serif;
      font-weight: 500;
      margin: 0 0 0.8em 0;
      padding: 0 0 0.2em 0;
    }

    p {
      color: #444;
      font-weight: 300;
      line-height: 1.6em;
    }

    p.borderBelow {
      border-bottom: 1px solid #eee;
      padding: 0 0 20px 0;
    }

    a#twitter svg {
      height: 40px;
      width: 40px;
    }

    @media (max-width: 650px) {
      h1 {
        font-size: 24px;
      }
    }

    @media (max-width: 550px) {
      h1 {
        font-size: 22px;
      }
    }

    @media (max-width: 450px) {
      h1 {
        font-size: 20px;
      }
    }
  </style>

  <base target="_blank">

</head>

<body>

  <div id="container">
    <!--     <div id="highlight">
        <p>Subscribe to my free newsletter for audio, video and realtime.</p>
        <p>Sign up: <a href="http://bit.ly/signupmedia" title="Newsletter sign-up">bit.ly/signupmedia</a>.</p>
        <p>Archive: <a href="http://medianews.me" title="Newsletter archive">medianews.me</a>.﻿</p>
      </div> -->

    <div id="highlight">
      <p>New(ish) article:
        <a href="https://medium.com/dev-channel/how-to-add-full-text-search-to-your-website-4e9c80ce2bf4">How to add search to your website</a>
      </p>
    </div>

    <h1>simpl.info</h1>

    <a id="twitter" href="https://twitter.com/intent/follow?original_referer=http%3A%2F%2Fsimpl.info%2F&ref_src=twsrc%5Etfw&region=follow_link&screen_name=sw12&tw_p=followbutton"
      rel="noopener" target="_blank" title="Follow @sw12">
      <svg viewbox="0 0 400 400">
        <title>Follow @sw12</title>
        <path d="M153.62,301.59c94.34,0,145.94-78.16,145.94-145.94,0-2.22,0-4.43-.15-6.63A104.36,104.36,0,0,0,325,122.47a102.38,102.38,0,0,1-29.46,8.07,51.47,51.47,0,0,0,22.55-28.37,102.79,102.79,0,0,1-32.57,12.45,51.34,51.34,0,0,0-87.41,46.78A145.62,145.62,0,0,1,92.4,107.81a51.33,51.33,0,0,0,15.88,68.47A50.91,50.91,0,0,1,85,169.86c0,.21,0,.43,0,.65a51.31,51.31,0,0,0,41.15,50.28,51.21,51.21,0,0,1-23.16.88,51.35,51.35,0,0,0,47.92,35.62,102.92,102.92,0,0,1-63.7,22A104.41,104.41,0,0,1,75,278.55a145.21,145.21,0,0,0,78.62,23"
          fill="#1da1f2" />
      </svg>
      <div>Follow on Twitter</div>
    </a>

    <p>This site aims to provide simplest possible examples of HTML, CSS and JavaScript.</p>

    <p>There are shortcuts for many of these pages (see
      <a href="shortcuts" title="Full list of redirect URL shortcuts">full list</a>). For example,
      <a href="https://simpl.info/v" title="Video element demo">simpl.info/v</a> redirects to
      <a href="https://simpl.info/video" title="Video element demo">simpl.info/video</a>.</p>

    <p>A list of web development resources is available from
      <a href="http://bit.ly/webdevres" title="Document with links to web development resources">bit.ly/webdevres</a>.</p>

    <p class="borderBelow">Submit bug reports, requests and comments at
      <a href="https://github.com/samdutton/simpl" title="simpl.info github repo">github.com/samdutton/simpl</a>.</p>

    <div id="links">
      <a href="xhr" title="Ajax (aka XMLHttpRequest) example">Ajax (aka XMLHttpRequest)</a>
      <a href="appcache" title="Application Cache">AppCache</a>
      <a href="array" title="Array methods">Array methods: some, every, filter, forEach, map</a>
      <a href="audio" title="Audio element">&lt;audio&gt;</a>
      <a href="audiodata" title="Audio Data API">Audio Data</a>
      <a href="battery" title="Battery API">Battery API</a>
      <a href="canplaytype" title="canPlayType()">canPlayType()</a>
      <a href="canvas" title="Canvas element example">&lt;canvas&gt;</a>
      <a href="cors" title="CORS demo, using XMLHttpRequest">CORS with XHR</a>
      <a href="cssfilters" title="CSS filters">CSS filters</a>
      <a href="flexboxcenter" title="CSS Flexbox center">CSS Flexbox: center</a>
      <a href="flexboxexpand" title="CSS Flexbox expand-to-fit example">CSS Flexbox: expand to fit</a>
      <a href="grid" title="CSS Grid simple example">CSS Grid: simple example</a>
      <a href="gridpage" title="CSS Grid page layout example">CSS Grid: page layout</a>
      <a href="cssnegativeselector" title="CSS negative selector example">CSS negative selector</a>
      <a href="cssregions" title="CSS regions example">CSS regions</a>
      <a href="csstextindent" title="CSS text-indent example">CSS text-indent</a>
      <a href="csstransition" title="CSS transition example">CSS transition</a>
      <a href="rtcdatachannel" title="RTCDataChannel example">Data channels</a>
      <a href="datalist" title="Input datalist element example">&lt;datalist&gt;</a>
      <a href="details" title="Details/summary element example">&lt;details&gt; and &lt;summary&gt;</a>
      <a href="devicemotion" title="Device Motion example">Device Motion</a>
      <a href="deviceorientation" title="Device Orientation example">Device Orientation</a>
      <a href="eme/clearkey" title="EME Clear Key example">Encrypted Media Extensions (EME) Clear Key</a>
      <a href="eventsource" title="EventSource (Server-Sent Events) example">EventSource (aka Server-Sent Events)</a>
      <a href="fetch" title="Fetch API example">Fetch</a>
      <a href="localstorage" title="Fieldset example">Fieldset (localStorage example)</a>
      <a href="filesystem" title="FileSystem example">FileSystem</a>
      <a href="filesystem/blob" title="FileSystem example using the Blob API">FileSystem using Blob</a>
      <a href="fullscreen" title="Fullscren">Fullscreen</a>
      <a href="search/lunr" title="Fullscren">Full text offline search with Elasticlunr</a>
      <a href="search/pouchdb" title="Fullscren">Full text offline search with PouchDB</a>
      <a href="geolocation" title="Geolocation example">Geolocation</a>
      <a href="https://www.simpl.info/getusermedia" title="getUserMedia() example">getUserMedia</a>
      <a href="https://www.simpl.info/getusermedia/constraints" title="getUserMedia() example with constraints">getUserMedia: choose resolution</a>
      <a href="https://www.simpl.info/getusermedia/sources" title="getUserMedia() example using MediaStreamTrack.getSources()">getUserMedia: select camera and microphone</a>
      <a href="history" title="History method example">History pushState() and popState()</a>
      <a href="softhyphen" title="Soft hyphen (&amp;shy;) example">Hyphenation (soft hyphen)</a>
      <a href="iframe" title="iframe element example">&lt;iframe&gt;</a>
      <a href="bigimage" title="Example of an image with large file size">Image: a big one (20MB)</a>
      <a href="imagecapture" title="ImageCapture example: take a photo">ImageCapture</a>
      <a href="idbkeyval" title="IndexedDB IDB-Keyval example">IndexedDB: IDB-Keyval</a>
      <a href="inputtypes" title="Examples of input elements with different types">Input types: email, tel, url, date, time, colour</a>
      <a href="install" title="beforeinstallprompt deferral example">Install prompt handling</a>
      <a href="intersectionobserver" title="Intersection Observer example">Intersection Observer</a>
      <a href="lazy" title="Using Intersection Observer to lazy load images">Intersection Observer: lazy load images</a>
      <a href="localstorage" title="localStorage">localStorage</a>
      <a href="mediacapture" title="Media Capture API">Media Capture (using &lt;input&gt;)</a>
      <a href="mediafragments" title="Media Fragments API">Media Fragments</a>
      <a href="mediaqueries" title="Media Queries demo">Media Queries</a>
      <a href="mse" title="Media Source Extensions example">Media Source Extensions (MSE)</a>
      <a href="getusermedia/sources" title="getUserMedia() example using MediaStreamTrack.getSources()">MediaStreamTrack.getSources()</a>
      <a href="mediarecorder" title="MediaStream Recording API">MediaRecorder</a>
      <a href="mutationobserver" title="MutationObserver example">MutationObserver</a>
      <a href="observe" title="Object.observe() example">Object.observe()</a>
      <a href="navigationtiming" title="Navigation Timing demo">Navigation Timing (window.performance)</a>
      <a href="useragent" title="navigator.userAgent">navigator.userAgent</a>
      <a href="online" title="Online API example">navigator.online</a>
      <a href="notification" title="Notification API example">Notification</a>
      <a href="pagevisibility" title="Page Visibility API example">Page Visibility API</a>
      <a href="pictureart" title="Picture element art direction example">&lt;picture&gt; for art direction</a>
      <a href="picturetype" title="Picture element alternative sources example">&lt;picture&gt; with alternative file types</a>
      <a href="postmessage" title="postMessage() example">postMessage()</a>
      <a href="promises" title="Promises example">promises</a>
      <a href="queryselector" title="querySelector() and querySelectorAll() examples">querySelector() and querySelectorAll()</a>
      <a href="resourcetiming" title="Resource Timing demo">Resource Timing</a>
      <a href="rtcdatachannel" title="RTCDataChannel">RTCDataChannel (WebRTC)</a>
      <a href="rtcpeerconnection" title="RTCPeerConnection">RTCPeerConnection (WebRTC)</a>
      <a href="getusermedia/screencapture" title="getUserMedia screen capture example">Screen capture</a>
      <a href="scrollintoview" title="scrollIntoView() example">scrollIntoView()</a>
      <a href="eventsource" title="EventSource (Server-Sent Events) example">Server-Sent Events (aka EventSource)</a>
      <a href="serviceworker" title="sessionStorage example">ServiceWorker</a>
      <a href="sizeswvalues" title="img element: sizes attribute with srcset using w values">sizes attribute with srcset using w values</a>
      <a href="sessionstorage" title="sessionStorage example">sessionStorage</a>
      <a href="srcsetwvalues" title="img element with srcset attribute using w values">srcset: using w values with &lt;img&gt;</a>
      <a href="srcsetxvalues" title="img element with srcset attribute using x values">srcset: using x values with &lt;img&gt;</a>
      <a href="stt" title="Web Speech API: speech to text">speech recognition</a>
      <a href="tts" title="Web Speech API: text to speech">speech synthesis</a>
      <a href="svg" title="SVG example">SVG</a>
      <a href="track" title="Track element">&lt;track&gt; with &lt;video&gt;</a>
      <a href="track/audio" title="Track element for audio">&lt;track&gt; with &lt;audio&gt;</a>
      <a href="track/map" title="Track element with synchronised metadata">&lt;track&gt; to synchronise video playback with Google Maps &amp; Street View display</a>
      <a href="useragent" title="User agent example">user agent</a>
      <a href="vibrate" title="navigator.vibrate() example">Vibrate</a>
      <a href="video" title="Video element">&lt;video&gt; with autoplay</a>
      <a href="videoalpha" title="Video with alpha transparency">&lt;video&gt; with alpha transparency</a>
      <a href="video/events" title="All video element events">&lt;video&gt; events</a>
      <a href="video/scripted" title="Video with scripted playback">&lt;video&gt; with scripted playback</a>
      <a href="longvideo" title="Long video example (~380MB)">long video (~380MB)</a>
      <a href="video/multi" title="20+ video elements">multiple video elements</a>
      <a href="videomedia" title="Video media query attribute">video with src media query</a>
      <a href="video/overlay" title="Long video example (~380MB)">video with &lt;div&gt; overlay</a>
      <a href="video/preloadnone" title="Video with preload none attribute value">video with preload="none"</a>
      <a href="video/range" title="Video range request using the Fetch API">video range request</a>
      <a href="video/resize" title="Video resize demo">video resizing demo</a>
      <a href="webanimations" title="Web Animations">Web Animations</a>
      <a href="webaudio" title="Web Audio">Web Audio</a>
      <a href="webfonts" title="Web fonts">Web Fonts</a>
      <a href="webgl" title="Fullscren">WebGL</a>
      <a href="webp" title="WebP">WebP</a>
      <a href="webrtc" title="WebRTC home">WebRTC (getUserMedia, RTCPeerConnection, RTCDataChannel)</a>
      <a href="websocket" title="WebSocket">WebSocket</a>
      <a href="stt" title="Web Speech API: speech to text">Web Speech: speech recognition</a>
      <a href="tts" title="Web Speech API: text to speech">Web Speech: speech synthesis</a>
      <a href="websql" title="WebSQL">WebSQL</a>
      <a href="webworkers" title="Web Workers example">Web Workers</a>
      <a href="xhr" title="XMLHttpRequest (aka Ajax) example">XMLHttpRequest (aka Ajax)</a>
    </div>

    <a href="https://github.com/samdutton/simpl/blob/gh-pages/index.html" title="View source for this page on GitHub" id="viewSource">View source on GitHub</a>

    <script>
      if (navigator.serviceWorker) {
        navigator.serviceWorker.register('sw.js').catch(function (error) {
          console.error('Unable to register service worker.', error);
        });
      }
    </script>

  </div>
  <!-- container -->

</body>

</html>          
    """
    return HttpResponse(text)