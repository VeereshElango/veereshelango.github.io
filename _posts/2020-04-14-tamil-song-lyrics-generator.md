---
title: "Tamil song lyrics generator"
categories:
  - apps
tags:
  - nlp
  - text-generation
  - tamil
  -
classes: wide
read_time: false
include_style: tamil_song_style.html
excerpt: This applications generates song lyrics in tamil using machine learning model trained on 4142 tamil songs.
---
<p>This applications generates song lyrics in tamil using machine learning model trained on 4142 tamil songs.</p>

**Work on progress!** This site is under update to make it more user friendly.
{: .notice--danger}

<div class="row" >
  <div class="column side" style="background-color:#f5f0f5">
    Enter starting word in Tamil <input type="text" value="அன்னை " id="startText">
    Choose the diversity <input type="range" id="diversity" class="form-control-range" min="0.1" max="1" step="0.1" value="0.2">
    <label for="quantity">Number of characters</label>
    <input type="number" id="quantity" name="quantity" min="50" max="5000" value="100">
    <input type="button" onclick="generateLyrics()" class="btn btn--info" value="Generate Text">
  </div>
  <div class="column middle" >
    <p id="output"></p>
  </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.5.2/dist/tf.min.js"></script>
<script src="/assets/models/fullsongs_model_working/char_idx_converter.js"></script>
<script src="/assets/js/util.js"></script>
<script>

		tf.loadLayersModel('/assets/models/fullsongs_model_working/model.json').then(function(model) {
	      window.model = model;
	    });
    function generateLyrics(){
      var element = document.getElementById('output')
      var generatedString=""
      if(window.model){
          var textbox = document.getElementById("startText")
          var diversity = document.getElementById("diversity")
          var quantity = document.getElementById("quantity")
          generatedString = generate_text(element, window.model, textbox.value, char2idx, idx2char, diversity.value, quantity.value)
        }
       else{
          generatedString="Model not loaded";
       }
       element.innerHTML = generatedString
    }
</script>