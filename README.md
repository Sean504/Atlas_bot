<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Atlas AI Assistant 🤖</title>
   <link href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100">
   <div class="container mx-auto px-4 py-8 max-w-4xl">
       <header class="text-center mb-12">
           <h1 class="text-5xl font-bold mb-4">Atlas AI Assistant 🤖</h1>
           <p class="text-xl text-gray-600">Local Voice & Text AI Powered by Ollama 🚀</p>
       </header>

       <nav class="bg-white shadow-lg rounded-lg p-6 mb-8">
           <div class="flex justify-center space-x-4">
               <a href="#installation" class="text-blue-600 hover:text-blue-800">⚙️ Installation</a>
               <a href="#usage" class="text-blue-600 hover:text-blue-800">📱 Usage</a>
               <a href="#features" class="text-blue-600 hover:text-blue-800">✨ Features</a>
               <a href="#troubleshooting" class="text-blue-600 hover:text-blue-800">🔧 Troubleshooting</a>
           </div>
       </nav>

       <section id="features" class="bg-white rounded-lg shadow-lg p-8 mb-8">
           <h2 class="text-3xl font-bold mb-6">✨ Features</h2>
           <div class="grid md:grid-cols-2 gap-6">
               <div class="border rounded-lg p-4">
                   <h3 class="text-xl font-semibold mb-3">🎯 Core Features</h3>
                   <ul class="list-disc pl-5 space-y-2">
                       <li>🗣️ Voice & Text Interaction</li>
                       <li>🤖 Local AI Processing</li>
                       <li>💻 Code Generation</li>
                       <li>🔧 System Tools</li>
                       <li>📊 Visual Feedback</li>
                   </ul>
               </div>
               <div class="border rounded-lg p-4">
                   <h3 class="text-xl font-semibold mb-3">🛠️ Technical Features</h3>
                   <ul class="list-disc pl-5 space-y-2">
                       <li>🎤 Wake Word Detection</li>
                       <li>🔊 Multi-device Audio</li>
                       <li>🧠 Model Selection</li>
                       <li>📝 Conversation Logging</li>
                       <li>⚡ Real-time Processing</li>
                   </ul>
               </div>
           </div>
       </section>

       <section id="installation" class="bg-white rounded-lg shadow-lg p-8 mb-8">
           <h2 class="text-3xl font-bold mb-6">⚙️ Installation</h2>
           <div class="space-y-6">
               <div>
                   <h3 class="text-xl font-semibold mb-3">📋 Prerequisites</h3>
                   <div class="bg-gray-100 rounded p-4">
                       <ul class="list-disc pl-5 space-y-2">
                           <li>🖥️ Raspberry Pi / Linux</li>
                           <li>🐍 Python 3.8+</li>
                           <li>🎤 Microphone</li>
                           <li>🔊 Speaker</li>
                           <li>📺 ST7789 Display (optional)</li>
                       </ul>
                   </div>
               </div>
               <div>
                   <h3 class="text-xl font-semibold mb-3">📥 Quick Install</h3>
                   <div class="bg-gray-800 text-white rounded p-4 font-mono">
                       <pre class="whitespace-pre-wrap">
chmod +x install.sh
./install.sh
source atlas_env/bin/activate</pre>
                   </div>
               </div>
           </div>
       </section>

       <section id="usage" class="bg-white rounded-lg shadow-lg p-8 mb-8">
           <h2 class="text-3xl font-bold mb-6">📱 Usage</h2>
           <div class="space-y-6">
               <div>
                   <h3 class="text-xl font-semibold mb-3">🚀 Getting Started</h3>
                   <div class="bg-gray-100 rounded p-4">
                       <ol class="list-decimal pl-5 space-y-2">
                           <li>Select Mode (Voice/Terminal)</li>
                           <li>Choose AI Model</li>
                           <li>Configure Audio Devices (Voice Mode)</li>
                           <li>Start Interacting!</li>
                       </ol>
                   </div>
               </div>
               <div>
                   <h3 class="text-xl font-semibold mb-3">💬 Commands</h3>
                   <div class="overflow-x-auto">
                       <table class="min-w-full table-auto">
                           <thead>
                               <tr class="bg-gray-100">
                                   <th class="px-4 py-2">Type</th>
                                   <th class="px-4 py-2">Command</th>
                                   <th class="px-4 py-2">Example</th>
                               </tr>
                           </thead>
                           <tbody>
                               <tr>
                                   <td class="border px-4 py-2">💻 Code</td>
                                   <td class="border px-4 py-2">generate/create</td>
                                   <td class="border px-4 py-2">"generate python calculator"</td>
                               </tr>
                               <tr>
                                   <td class="border px-4 py-2">📁 Files</td>
                                   <td class="border px-4 py-2">write/read</td>
                                   <td class="border px-4 py-2">"write hello to file.txt"</td>
                               </tr>
                               <tr>
                                   <td class="border px-4 py-2">🔧 System</td>
                                   <td class="border px-4 py-2">run/execute</td>
                                   <td class="border px-4 py-2">"run ls -la"</td>
                               </tr>
                           </tbody>
                       </table>
                   </div>
               </div>
           </div>
       </section>

       <section id="troubleshooting" class="bg-white rounded-lg shadow-lg p-8 mb-8">
           <h2 class="text-3xl font-bold mb-6">🔧 Troubleshooting</h2>
           <div class="space-y-4">
               <details class="bg-gray-100 rounded p-4">
                   <summary class="font-semibold cursor-pointer">🎤 Audio Issues</summary>
                   <div class="mt-2 pl-4">
                       <pre class="bg-gray-800 text-white p-2 rounded">
arecord -l   # List inputs
aplay -l    # List outputs
groups | grep audio   # Check permissions</pre>
                   </div>
               </details>
               <details class="bg-gray-100 rounded p-4">
                   <summary class="font-semibold cursor-pointer">🤖 Model Issues</summary>
                   <div class="mt-2 pl-4">
                       <pre class="bg-gray-800 text-white p-2 rounded">
ollama list  # Check models
ls ~/.ollama/models   # Verify files</pre>
                   </div>
               </details>
               <details class="bg-gray-100 rounded p-4">
                   <summary class="font-semibold cursor-pointer">📺 Display Issues</summary>
                   <div class="mt-2 pl-4">
                       <pre class="bg-gray-800 text-white p-2 rounded">
sudo raspi-config  # Enable SPI
lsmod | grep spi   # Check module</pre>
                   </div>
               </details>
           </div>
       </section>

       <footer class="text-center text-gray-600 mt-12">
           <p>MIT License 📝 | Created with ❤️ using Ollama & Vosk</p>
       </footer>
   </div>
</body>
</html>
