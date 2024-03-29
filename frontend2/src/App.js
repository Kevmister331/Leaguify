import React, { useState, useEffect } from "react"
import items from "./assets/champions.json" // Adjust the import path as needed
import "./App.css"
import logo from './assets/leaguifylogo.png';
import loadingGif from './assets/teemo-league-of-legends.gif'; // Adjust the path as necessary


const BACKEND_URL = "http://127.0.0.1:5000"

const App = () => {
  const [loading, setLoading] = useState(false)
  const [selectedItem, setSelectedItem] = useState("Aatrox")
  const [selectedType, setSelectedType] = useState("Songs")
  const [songs, setSongs] = useState([])

  useEffect(() => {
    console.log(songs)
  }, [songs])

  const submitOptions = () => {
    if (selectedItem === "" || selectedType === "") {
      console.log("error submitting options, some still null")
    }
    setLoading(true)
    console.log("Submitting options:", selectedItem, selectedType)

    const URL = BACKEND_URL + `/getsongs/${selectedItem}`
    // + "/" + "headers"
    console.log(URL)
    // fetch(URL, {
    //   method: "GET",
    // })
    //   .then((result) => {
    //     console.log(result + "success")
    //     return
    //   })
    //   .catch((err) => {
    //     console.log(err)
    //   })
    // ,
    //   body: JSON.stringify({
    //     champion: selectedItem
    //   })

    // Make your API call here
    fetch(URL, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }
    }).then(response => response.json()) // This returns a Promise
      .then(data => {
        const result = data.songs; // Access the songs array
        console.log(result);       // Do something with the songs array
        setSongArray(result)
        setLoading(false)
      })
      .catch((err) => {
        console.log(err)
        setLoading(false)
      })
  }

  const setSongArray = (songs) => {
    let correctlyFormattedSongs = []
    songs.map((song) => {
      let correctlyFormattedSong = {title: "", artist: "", url: "", artistUrl: ""}
      // song title
      correctlyFormattedSong["title"] = song['song']
      console.log(song)
      console.log(song.song)
      console.log(song['song'])
      console.log(song['artist'])
      // artist name
      correctlyFormattedSong["artist"] = song['artist']
      // song url
      correctlyFormattedSong["url"] = song['searchResult']['tracks']['items'][0]['external_urls']['spotify']
      // artist url
      correctlyFormattedSong["artistUrl"] = song['searchResult']['tracks']['items'][0]['artists'][0]['external_urls']['spotify']
      correctlyFormattedSongs.push(correctlyFormattedSong)
    })
    // for (let song in songs) {
    //   let correctlyFormattedSong = {title: "", artist: "", url: ""}
    //   // song name
    //   correctlyFormattedSong["title"] = song['song']
    //   console.log(song)
    //   console.log(song.song)
    //   console.log(song['song'])
    //   console.log(song['artist'])
    //   // artist name
    //   correctlyFormattedSong["artist"] = song['artist']
    //   // song url
    //   correctlyFormattedSong["url"] = song['searchResult']['tracks']['items'][0]['external_urls']['spotify']
    //   correctlyFormattedSongs.push(correctlyFormattedSong)
    // }
    setSongs(correctlyFormattedSongs)
  }

  const handleDropdownChange = (event) => {
    setSelectedItem(event.target.value)
  }

  const handleTypeChange = (event) => {
    setSelectedType(event.target.value)
  }

  return (
    <div className="background">
      <div className="container">
        <img src={logo} alt="Leaguify Logo" className="logo" />
        <h2>Leaguify</h2>
        <div className="dropdown-container">
          <div className="dropdown-group">
            <h3>Select Champion</h3>
            <select value={selectedItem} onChange={handleDropdownChange}>
              {items.map((item) => (
                <option key={item.name} value={item.name}>
                  {item.name}
                </option>
              ))}
            </select>
          </div>
          <div className="dropdown-group">
            <h3>Select output type</h3>
            <select value={selectedType} onChange={handleTypeChange}>
              <option value="Songs">Songs</option>
              <option value="Albums">Albums</option>
              <option value="Artists">Artists</option>
            </select>
          </div>
        </div>
        <button className="button" onClick={submitOptions} disabled={loading}>
          Generate
        </button>
        {loading && <img src={loadingGif} alt="Loading..." />}
        {loading && <p >Generating...</p>}
        
      </div>

      <div className="song-list-container">
        <h1>Result</h1>
        <p>Get the top tracks related to your champion!</p>
        <ul className="song-list">
          {songs.map((song, index) => (
            <li key={index} className="song-item">
              <span className="song-rank">{index + 1}</span>
              <a href={song.url} className="song-title" target="_blank" rel="noreferrer">
                {song.title}
              </a>
              <a href={song.artistUrl} className="song-artist" target="_blank" rel="noreferrer">
                {song.artist}
              </a>
            </li>
          ))}
        </ul>
      </div>
    </div>
  )
}

export default App
