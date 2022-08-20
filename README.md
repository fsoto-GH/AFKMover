<h1>AFKMover</h1>
Little tool to keep your computer from sleeping (in a human-like manner). Allows you to specify a stop time and ability to shut down. 

<h2>Requirements</h2>
<p>It is highly advised to have PIP installed, but you can definitely install the required package(s) manually.</p>

<h2>How to Run</h2>
<p>Ensure you have the required packages found in the <code>requirements.txt</code>. 
If you have pip, you can run <code>pip install -r requirements.txt</code>.</p>

<p>You can execute the app using the following command: 
<code>py move_k.py [[st=sleep_time] [tm=hh:mm:ss[AM|PM]] [sd=seconds]]</code></p>
<ul>
    <li><code>st</code> - the interval between key presses in seconds</li>
    <ul>
        <li>If none is specified, the default of 2 seconds is applied.</li>    
    </ul>
    <li><code>tm</code> - the time at which the program should stop running</li>
    <ul>
        <li>If none is specified, then the program will execute until a keyboard interrupt.</li>    
    </ul>
    <li><code>sd</code> - the amount of time in seconds, after <code>tm</code>, to shut down the computer</li>
    <ul>
        <li>If none is specified, then the program will simply exit at the shutdown time.</li>
        <li>A <code>tm</code> is required for this parameter.</li>
    </ul>
    <li>If no argument is specified, the program will use the default sleep time and execute untila keyboard interrupt 
    is triggered.</li>
</ul>

<p>You can also run <code>py move_k.py --help</code> to obtain usage information via the command line.</p>

<h3>Example</h3>
<ul style="list-style: none;">
    <li><code>py move_k.py</code> - run for an undefined amount of time, key-pressing at the default sleep time interval.</li>
    <li><code>py move_k.py st=10</code> - run for an undefined amount of time key-pressing every 10 seconds.</li>
    <li><code>py move_k.py tm=10:00:00AM</code> - run until 10:00:00AM system time then exit program with default sleep time.</li>
    <li><code>py move_k.py tm=10:00:00AM sd=10</code> - run until 10:00:00AM system time and shutdown 10 seconds after, using default sleep time.</li>
    <li><code>py move_k.py tm=10:00:00AM sd=10 st=20</code> - run until 10:00:00AM system time, shutdown 10 seconds after, key-pressing every 20 seconds</li>
</ul>
