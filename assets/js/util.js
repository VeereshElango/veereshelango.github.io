const modelPath = "/assets/models/<MODELNAME>/model.json"
const modelDict = {
  "allSongs": modelPath.replace("<MODELNAME>","fullsongs_model_working"),
  "kannadasan":modelPath.replace("<MODELNAME>","kannadasan_model"),
  "vairamuthu":modelPath.replace("<MODELNAME>","vairamuthu_model"),
  "vaali":modelPath.replace("<MODELNAME>","vaali_model")
}
function loadModel(){
    event.preventDefault();
    document.getElementById('loadModelButt').disabled=true;
    setStatusMessage("Please wait while loading. The model takes nearly 60sec to load.","modelLoadingOutput");
    setStatusMessage("","output");
    setTimeout(function () {
        var modelChoice = document.getElementById("modelChoice").value

        if(modelChoice.value === ""){
        }
        else{
          tf.loadLayersModel(modelDict[modelChoice]).then(function(model) {
             window.model = model;
             setStatusMessage(modelChoice.charAt(0).toUpperCase()+modelChoice.slice(1)+" Model Loaded","modelLoadingOutput");
             document.getElementById('loadModelButt').disabled=false;
          });
        }
        console.log("inside timeout")
    }, 100);

    console.log(window.model)
}
function generateLyrics(event){
        event.preventDefault();
        document.getElementById('genTextBut').disabled=true;
        setStatusMessage('Please wait while generating...','output');
        setTimeout(function () {
            var textbox = document.getElementById("startText")
            console.log(textbox.value)
            if(textbox.value === ""){
                document.getElementById("valError").innerText = "Field is empty.";
                setStatusMessage('Enter a starting word or phrase.','output');
            }
            else if(window.model){
              document.getElementById("valError").innerText = "";
              var diversity = document.getElementById("diversitySlider")
              var quantity = document.getElementById("quantity")
              var modelChoice = document.getElementById("modelChoice").value
              generatedString = generate_text(window.model, textbox.value, char2idx[modelChoice], idx2char[modelChoice], diversity.value, quantity.value)
              setStatusMessage(generatedString,'output');
            }
            else{
              setStatusMessage('Model not loaded. Please choose the model from drop down and click load model.','output');
            }
            document.getElementById('genTextBut').disabled=false;
        }, 100);
    }
function generate_text(model, start_string, char2idx, idx2char, temperature=1.0, num_characters = 100){
  // Number of characters to generate
  num_generate = num_characters

  // Converting our start string to numbers (vectorizing)
  input_eval = []
  for (s of start_string){input_eval.push(char2idx[s])}
  input_eval = tf.expandDims(input_eval, 0)
  // Empty string to store our results
  text_generated = []

  // Low temperatures results in more predictable text.
  // Higher temperatures results in more surprising text.
  // Experiment to find the best setting.

  // Here batch size == 1
  model.resetStates()
  for (var i=0; i<num_generate; i++) {
      //console.log("Input eval", input_eval.toString())
      predictions = model.predict(input_eval)
      // remove the batch dimension
      predictions = tf.squeeze(predictions, 0)
      //console.log("Predictions : ",predictions.toString())
      // using a categorical distribution to predict the character returned by the model
      predicted_id = sample(predictions, temperature)
      //console.log("Predicted ID",predicted_id)
      // We pass the predicted character as the next input to the model
      // along with the previous hidden state
      input_eval = tf.expandDims([predicted_id], 0)
      generatedCharacter = idx2char[predicted_id]
      //console.log("Next :", generated_character)
      if(text_generated[text_generated.length - 1] === "</br>" & generatedCharacter === "</br>"){
        i--
        }
      else{
        text_generated.push(generatedCharacter)
      }
    }
  return (start_string + text_generated.join(""))
}
function sample(probs, temperature)  {
    logits = tf.div(predictions, Math.max(temperature, 1e-6));
    //console.log(logits)
    var isNormalized = false;
    // `logits` is for a multinomial distribution, scaled by the temperature.
    // We randomly draw a sample from the distribution.
    return tf.multinomial(logits, 1, null, isNormalized).dataSync()[0];
  };

