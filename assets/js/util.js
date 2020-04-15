function generate_text(model, start_string, char2idx, idx2char, temperature=1.0, num_characters = 100){
  // Evaluation step (generating text using the learned model)

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
         /*var evt = document.createEvent("Event");
        evt.initEvent("myEvent",true,true);
        // custom param
        evt.foo = generatedCharacter;
        //register
        document.addEventListener("myEvent",myEventHandler,false);
        //invoke
        document.dispatchEvent(evt);*/
        text_generated.push(generatedCharacter)
      }
    }
  return (start_string + text_generated.join(""))
}

function appendText(c){
  console.log("Appendedv: "+c)
  var element = document.getElementById('output')
  element.textContent += c;
}
function myEventHandler(e){
//  appendText(e.foo);
  var element = document.getElementById('output')
  element.textContent += e.foo;
}


function sample(probs, temperature)  {
    logits = tf.div(predictions, Math.max(temperature, 1e-6));
    //console.log(logits)
    var isNormalized = false;
    // `logits` is for a multinomial distribution, scaled by the temperature.
    // We randomly draw a sample from the distribution.
    return tf.multinomial(logits, 1, null, isNormalized).dataSync()[0];
  };

