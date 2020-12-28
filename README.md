# NewsHeadlines

The aim of this project is to grab headlines from the NYTimes API and display them to a RGB LED Matrix Display using a raspberry pi. You will need python 3 installed as well as the "Requests" python package installed.

## Using the config file

1.) Copy `template.config.json` and remae as `config.json`

2.) Add your API Key from NYTimes into the `api_Key` field. You can sign up for the API [here](https://developer.nytimes.com/)

<table>
<tr>
<th>Variable</th>
<th>Useage</th>
</tr>
<tr>
<td>api_key</td>
<td> <code>"NYTimes Api Key"</code> </td>
</tr>
<tr>
<td>section</td>
<td> If you want one section, simply enter <code>"us"</code> <br> If you want multiple sections, enter them as a list <code>["us", "world"]</code> <br> List of sections: <i>arts, automobiles, books, business, fashion, food, health, home, insider, magazine, movies, nyregion, obituaries, opinion, politics, realestate, science, sports, sundayreview, technology, theater, t-magazine, travel, upshot, us, and world.</i> </td>
</tr>
<tr>
<td>Number_of_Headlines</td>
<td> You can enter an int here such as <code>"2"</code>. This will show 2 articles for each section selected. If you want to view all articles for each section selected, enter <code>"all"</code>. </td>
</tr>
</table>