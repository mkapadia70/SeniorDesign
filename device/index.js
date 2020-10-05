const { app, BrowserWindow } = require('electron')


let pressed = true

function turnColor()
{
    if(document.getElementById("btn").innerHTML === "Unmute")
    {
        document.getElementById("btn").style.backgroundColor = "green";       
        document.getElementById("btn").style.color = "white"; 
    }
    else
    {
        document.getElementById("btn").style.backgroundColor = "red";       
        document.getElementById("btn").style.color = "white";       

    }
}

function turnBack()
{
  document.getElementById("btn").style.backgroundColor = "white"; 
  document.getElementById("btn").style.color = "black"; 
}

function toPython(vars) {
  var python = require('child_process').spawn('python', ['./Testing.py', vars]);
  python.stdout.on('data', function (data) {
    console.log("Python response: ", data.toString('utf8'));
    
  });

  python.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  python.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
  });
}

//changes color and text of button, also runs python code to mute/unmute audio
function muteUnmute() {
  pressed = !pressed;
  vars = ["muteUnmute", pressed]
  toPython(vars)
  if(!pressed)
    {
        document.getElementById("btn").innerHTML = "Unmute"
        document.getElementById("btn").style.backgroundColor = "green";       
        document.getElementById("btn").style.color = "white"; 
    }
    else
    {
        document.getElementById("btn").innerHTML = "Mute"
        document.getElementById("btn").style.backgroundColor = "red";       
        document.getElementById("btn").style.color = "white";       

    }
}

function updateAudio() {
  val = document.getElementById("testSlider").value
  vars = ["updateAudio", val]
  toPython(vars)
  if(!pressed)
    {
        document.getElementById("btn").innerHTML = "Unmute"
        document.getElementById("btn").style.backgroundColor = "green";       
        document.getElementById("btn").style.color = "white"; 
    }
    else
    {
        document.getElementById("btn").innerHTML = "Mute"
        document.getElementById("btn").style.backgroundColor = "red";       
        document.getElementById("btn").style.color = "white";       

    }
}



function createWindow () {
  // Create the browser window.
  const win = new BrowserWindow({
    width: 800,
    height: 400,
    webPreferences: {
      nodeIntegration: true
    }
  })
  //win.removeMenu() //uncomment in the final code

  win.loadFile('index.html')


}

app.whenReady().then(createWindow)


app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow()
  }
})





