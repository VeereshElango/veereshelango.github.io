var perplexities = ["10","30","50","100"],
ngrams={
    "Unigram":"1_1", "Unigram&Bigram":"1_2", "Unigram&Bigram&Trigram":"1_3",
    "Bigram":"2_2","Trigram":"3_3"
};

Plotly.d3.json('model/20_news_group_tsne_visualization.json', function(err, jsonObj){
		var perplexities = ["10","30","50","100"],
		ngrams={
			"Unigram":"1_1", "Unigram&Bigram":"1_2", "Unigram&Bigram&Trigram":"1_3",
			"Bigram":"2_2","Trigram":"3_3"
		},
		chosenPerplexity = "",
		chosenNgram="",
		targetNames = Object.keys(jsonObj),
		defaultPerplexity = perplexities[0]
		defaultNgrams = ngrams["Unigram"],
		target_color =['#2E91E5', '#E15F99', '#1CA71C', '#FB0D0D', '#DA16FF', '#222A2A', '#B68100', '#750D86', '#EB663B', '#511CFB', '#00A08B', '#FB00D1', '#FC0080', '#B2828D', '#6C7C32', '#778AAE', '#862A16', '#A777F1', '#620042', '#1616A7'],
		target_color_map = {};
		
		var c_i = 0;
		for(key in targetNames){
			target_color_map[key] = target_color[c_i]
			c_i++
		}
		
		function assignOptions(textArray, selector) {
		  for (var i = 0; i < textArray.length;  i++) {
		      var currentOption = document.createElement('option');
		      currentOption.text = textArray[i];
		      selector.appendChild(currentOption);
		  }
		}
		
		function updatePerplexity(){
		  plotOnDemand(countrySelector.value, chosenNgram);
		}
		function updateNgramMode(){
		  plotOnDemand(chosenPerplexity, ngrams[ngramSelector.value]);
		}
    
		function plotOnDemand(perplexity, ngram_mode){
			chosenPerplexity = perplexity
			chosenNgram = ngram_mode
			var data = [];
			for (var key in jsonObj){
				var comp1 = jsonObj[key][perplexity+'_'+ngram_mode+'_comp1'],
	    		comp2 = jsonObj[key][perplexity+'_'+ngram_mode+'_comp2'],
	    		text = jsonObj[key]["targetNames"]

				var trace = {
			        x: comp1,
	    		    y: comp2,	    		    
	        		mode: 'markers',
	        		type: 'scatter',
	        		text:text,
	        		marker:{
	        			opacity : 0.7,
	        			size: 4,
	        			color:target_color_map[key],
	        			line: {
					      color: 'rgb(255, 255, 255)',
					      width: 0.5
					    }
	        		},
	        		name: key
	      		};

			data.push(trace)
			}    

	      	var layout = {
	        	hovermode:'closest',
	        	height:550 ,
	        	legend: {
	        		"font": {
	        			"size": 10 
	        		}
	        	}
	        };
			Plotly.newPlot('plotdiv', data, layout, {showSendToCloud: true, responsive: true});

			var myPlot = document.getElementById('plotdiv'),
			hoverInfo = document.getElementById('hoverinfo');
			myPlot.on('plotly_hover', function(data){
		    	var infotext = data.points.map(function(d){
		    		targetGroup = jsonObj[d.data.name]
		    		data = getTextData(targetGroup, d)
		      		return (data);
		    	});
		  
		    	hoverInfo.innerHTML = infotext.join('<br/>');
			})
		 	.on('plotly_unhover', function(data){
		    	hoverInfo.innerHTML = '';
			});
		}

  		plotOnDemand(defaultPerplexity, defaultNgrams)
  		var ngramSelector = document.querySelector('.ngrams')
  		assignOptions(Object.keys(ngrams), ngramSelector)
  		ngramSelector.addEventListener('change', updateNgramMode, false);

  		var innerContainer = document.querySelector('[data-num="0"'),
		countrySelector = innerContainer.querySelector('.countrydata');
		assignOptions(perplexities, countrySelector);
		countrySelector.addEventListener('change', updatePerplexity, false);
		
		function getTextData(targetGroup, d){
			var comp1 = targetGroup[chosenPerplexity+"_"+chosenNgram+"_comp1"] 
			var comp2 = targetGroup[chosenPerplexity+"_"+chosenNgram+"_comp2"] 
			for(var i=0; i< comp1.length;i++){
	    			if((comp1[i] === d.x && comp2[i] === d.y) ){
	    				return "<kbd>"+d.data.name+"</kbd><br>"+targetGroup["data"][i]
	    				.replace("From","<br><mark>From</mark>")
	    				.replace("Subject","<br><mark>Subject</mark>")
	    				.replace("Lines","<br><mark>Lines</mark>")
	    				.replace("Organization","<br><mark>Organization</mark>");
	    			}
	    		}
	    	return "no data"
		}
		
	})

function appendPCAColumn(row, ngram, ngramValue){
    var col = document.createElement("td")
    var imageName = pca_plots.replace("NGRAM",ngramValue)
    col.innerHTML = "<img src='img/tsne_visualizations/"+imageName+"' class='img-rounded' alt='"+ngram+"' width='200' height='200'> "
    row.appendChild(col)
}

function appendTSNEColumns(row, ngram, ngramValue){
    for(var j=0; j<perplexities.length;j++){
        var col = document.createElement("td")
        var imageName = tsne_plots.replace("NGRAM",ngramValue).replace("PERPLEXITY",perplexities[j])
        console.log(imageName)
        col.innerHTML = "<img src='img/tsne_visualizations/"+imageName+"' class='img-rounded' alt='"+ngram+"_"+perplexities[j]+"' width='200' height='200'> "
        row.appendChild(col)
    }
}

function appendSideHeader(row, ngram){
    var col = document.createElement("td")
    col.innerHTML = "<span>"+ngram.replace(/&/g,"&<br>")+"</span>"
    col.style.fontSize = "small";
    row.appendChild(col)
}
function appendTopRow(row){
    var col = document.createElement("td")
    col.innerHTML = "<div></div>"
    row.appendChild(col)
    var col = document.createElement("td")
    col.innerHTML = "<div class='text-center'>PCA</div>"
    row.appendChild(col)
    for(var j=0; j<perplexities.length;j++){
        var col = document.createElement("td")
        col.innerHTML = "<div class='text-center'>t-SNE Perplexity-"+perplexities[j]+"</div>"
        row.appendChild(col)
    }
}
var plotTable = document.getElementById("tableGallery")

ngramsList = ["Unigram","Unigram&Bigram","Unigram&Bigram&Trigram",
                  "Bigram","Trigram"]
var tsne_plots = "t-SNE- 20News group - TfIdf - NGRAM- tSNE perplexity - PERPLEXITY.png"
var pca_plots = "PCA- 20News group - TfIdf - NGRAM.png"

var row = document.createElement("tr")
appendTopRow(row)
plotTable.appendChild(row)

for(var i=0; i<ngramsList.length ; i++){
    var ngram = ngramsList[i]
    var row = document.createElement("tr")
    appendSideHeader(row, ngram)
    appendPCAColumn(row, ngram, ngrams[ngram])
    appendTSNEColumns(row, ngram, ngrams[ngram])
    plotTable.appendChild(row)
}