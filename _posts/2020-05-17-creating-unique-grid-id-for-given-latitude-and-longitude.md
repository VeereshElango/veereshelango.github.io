---
title: Creating unique grid-id for given latitude and longitude
excerpt: "A equation to transform latitude and longitude into unique grid-id without using any external libraries."
comments: true
categories:
    - utilities
tags:
    - geo-spatial
header:
  overlay_image: /assets/images/grid_world.png
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

Given geo-spatial data, have you got into a  situation to do the analysis
on an area or city or country level? Have you wondered how to map the latitude and 
longitude information to unique grid id without any external libraries?
Then this might help you.

<div class="mapouter align-right">
    <div class="gmap_canvas">
        <iframe width="300" height="200" id="gmap_canvas" src="https://maps.google.com/maps?q=59.325025,%2018.070753&t=&z=15&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>
    </div>
    <style>
        .mapouter{position:relative;text-align:right;height:200px;width:300px;}
        .gmap_canvas {overflow:hidden;background:none!important;height:200px;width:300px;}
    </style>
</div> 

For example, let's take a sample coordinate and calculate the grid id for that.

59.325025, 18.070753 (one of my favourite location at Stockholm)





## What do the decimals in the coordinates mean?

Before getting into the calculation of grid-id, we should understand the details of the decimal points in the latitude and 
longitude coordinates.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/decimal_degrees_latlong.png" alt="A snapshot from Andrej Karpathy blog.">
  <figcaption>A snapshot from Wikipedia.</figcaption>
</figure> 

It's simple, isn't it. As the number of decimal points increase we are getting precise with the location.



## Problems in creating grid id using just lat and long

For simplicity, let's create grids of a country-like or equally large area like areas.

Then we can remove the decimals in the lat and long.
```
round(latitude), round(longitude)
```
59.0, 18.0

Since the values of lat and long has both positive and negative values, we cannot directly use them as grid id

Why? Let's see with some examples.

|                       |                                                   Grid-id                                                   ||
| Possible Combinations | round(latitude) * round(longitude) | round(latitude) - round(longitude) | round(latitude) + round(longitude) |
|-----------------------|------------------------------------|------------------------------------|------------------------------------|
| 59, 18                | 1062                               | 41                                 | 77                                 |
| -59,18                | -1062                              | -77                                | -41                                |
| 59, -18               | -1062                              | 77                                 | 41                                 |
| -59,-18               | 1062                               | -41                                | -77                                |


We can remove multiplication operation, as it produces duplicates within the possible combinations of the coordinates. 

There is also a problem with subtraction and addition because the same values could be produced in many possible ways. For example

| Combinations | Grid-Id |
|--------------|---------|
| 70,7         | 77      |
| 69,8         | 77      |
| 90,-13       | 77      |

**Why this is not possible?**

The space between every latitude circle is one and we need to fit 360 longitude sections within them. 

## Solution

So if we make the space between two latitude values large enough contain all longitude sections, then the problem gets solved.

Since we are considering, one unit space between latitudes and the same for longitudes
We transform our equation to
```
360 * round(lat) + round(long)
```

| round(lat) | round(long) | round(lat) + round(long) | 360 * round(lat)  | 360 * round(lat) + round(long) |
|------------|-------------|--------------------------|-------------------|--------------------------------|
| 59         | 18          | 77                       | 21240             | 21258                          |
| 59         | -18         | -41                      | 21240             | 21222                          |
| -59        | 18          | 41                       | -21240            | -21222                         |
| -59        | -18         | -77                      | -21240            | -21258                         |
| 70         | 7           | 77                       | 25200             | 25207                          |


Thus by multiplying latitude with 360 we are able to generate unique grid id for all possible longitude.

```
GRID_ID = 360 * DEGREE * ROUND(LAT*DEGREE) + ROUND(LONG*DEGREE)
```

I would like to thank my colleague [Jakob Rogstadius](https://se.linkedin.com/in/jakobrogstadius) for passing
on this knowledge to me. 