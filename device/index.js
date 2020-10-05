const { app, BrowserWindow } = require('electron');
const querystring = require('querystring');


let { PythonShell } = require('python-shell');
let process = require('child_process')

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


//changes color and text of button, also runs python code to mute/unmute audio
function muteUnmute() {
  startPythonPersistent()
  pressed = !pressed;
  vars = ["muteUnmute", pressed]
  //toPython(vars)
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
  toPython(document.getElementById("testSlider").value)

}

function startPythonPersistent() {
  console.log("python")
  var python = require('child_process').spawn('python', ['./server.py']);
  python.stdout.on('data', function (data) {
    console.log("Python response: ", data.toString('utf8'));
    
  });

  python.stderr.on('data', (data) => {
    
  });

  python.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
  });
  
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



