var voiceIcon, transcriptElt, queryText, queryMessage; 

var result, loader, address;
var offset = 0;

var startSound = new Audio("/static/main/sound/hound_start.wav");
var stopSound = new Audio("/static/main/sound/hound_stop.wav");

$(document).ready(function(){
  voiceIcon = document.getElementById("voice-icon");
  transcriptElt = document.getElementById("query");
  queryText = document.getElementById("query_text");
  queryMessage = document.getElementById("query_message");

  result = document.getElementById("result");
  loader = document.getElementById("loader");
  address = document.getElementById("address");
});

var preAddress = "";
function get_restaurants(address) {
  if (address == "next") {
    offset = offset + 20;
    address = preAddress;
  } else if (address == "previous"){
    offset = offset - 20;
    address = preAddress;
  } else {
    offset = 1;
  }

  loader.style.display = "block";

  $.ajax({
    url: "/restaurants2",
    type: "get",
    data: {
      address: address,
      offset: offset
    },
    success: function(response) { 
      loader.style.display = "none";
      result.innerHTML = response; 
      result.style.display = "block";
      preAddress = address;
    },
    error: function(xhr) { 
      loader.style.display = "none";
      result.innerHTML = "<h2>ERROR</h2>";
      result.style.display = "block";
      preAddress = address;
    }
  });
}

function getAddress(query) {
    //if (query.startsWith("find restaurants near")) 
    //    return "";
    //if (query.startsWith("show me restaurants near")) 
    //    return "";
    //if (query.startsWith("find restaurants around")) 
    //    return "";
    //if (query.startsWith("show me restaurants near")) 
    //    return "";

    return query;
}


var clientID = "uNiHfl9SCEeYiznrEi9UHg==";

var requestInfo = { 
  ClientID: clientID,
  UserID: "find_restaurants",
  StoredGlobalPagesToMatch: ["restaurants"]
};

var myClient = new Houndify.HoundifyClient({

  clientId: clientID, 
  authURL: "/houndifyAuth",
  enableVAD: true,

  textSearchProxy: {
    url: "/textSearchProxy",
    method: "POST",
  },

  onResponse: function(response, info) {
    if (response.AllResults && response.AllResults[0] !== undefined) {
      var address = getAddress(transcriptElt.innerHTML);
      get_restaurants(address);
      queryText.innerHTML = "\"" + transcriptElt.innerHTML + "\"";
      transcriptElt.innerHTML = "";
    }
  },

  onError: function(err, info) {
    voiceIcon.src="/static/main/img/voice.svg";
  },

  onTranscriptionUpdate: function(trObj) {
    var transcriptElt = document.getElementById("query");
    transcriptElt.innerHTML = trObj.PartialTranscript;
  },

  onAbort: function(info) {},

  onRecordingStarted: function() {
    voiceIcon.src="/static/main/img/recording.png";
    startSound.play();
    queryText.innerHTML = "";
    result.style.display = "none";
  },

  onRecordingStopped: function() {
    voiceIcon.src="/static/main/img/voice.svg";
    stopSound.play();
  },

  onAudioFrame: function(frame) {}
});

function startStopVoiceSearch() {
  if (myClient.voiceSearch.isStreaming()) {
    myClient.voiceSearch.stop();
  } else {
    myClient.voiceSearch.startRecording(requestInfo);
  }
}

