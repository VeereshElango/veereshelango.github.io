---
layout: splash
permalink: /timeline/
title: "Timeline"
excerpt: "Minimal Mistakes is a flexible two-column Jekyll theme."
---

<link title="timeline-styles" rel="stylesheet" 
              href="https://cdn.knightlab.com/libs/timeline3/latest/css/timeline.css">
<script src="https://cdn.knightlab.com/libs/timeline3/latest/js/timeline.js"></script>
<style>
    .tl-timeline{
        height: 250px;
    }
    .tl-timegroup .tl-timegroup-message{
        color:black;
    }
    
</style>
<div id='timeline-embed' style="width: 100%; height: 600px"></div>

<script type="text/javascript">
    var options = {
        scale_factor:1              
        }
    // The TL.Timeline constructor takes at least two arguments:
    // the id of the Timeline container (no '#'), and
    // the URL to your JSON data file or Google spreadsheet.
    // the id must refer to an element "above" this code,
    // and the element must have CSS styling to give it width and height
    // optionally, a third argument with configuration options can be passed.
    // See below for more about options.
    timeline = new TL.Timeline('timeline-embed',
    'https://docs.google.com/spreadsheets/d/1fpOgknf3Vw98YjMTQ5SmfXqOt5t5PoqnpSQf5u_axu0/edit#gid=0', options);
</script>