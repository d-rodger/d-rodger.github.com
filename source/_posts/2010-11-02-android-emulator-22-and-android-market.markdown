---
layout: post
title: "Android Emulator 2.2 and Android Market"
date: 2010-11-02 17:20
comments: true
categories: [android, google, emulator, market]
---
<p>
One of the drawbacks to not having an actual Android phone (for now) is that I want to see what apps are available, but Google only has a sampling of what’s available on their <a href="http://www.android.com/market/" title="Android Market" target="_blank">web site</a>. I find that rather annoying.
</p>

<p>
Of course, I do have the emulator, and in theory I should be able to do something with that. The emulator does not come with Market access, but there are system images of the virtual devices for v1.5 and 1.6.
</p>

<p>
I have the v1.5, and it’s ok, but I wanted to see what was available for v2.2, which now has <a href="http://developer.android.com/resources/dashboard/platform-versions.html" title="android versions" target="_blank">36% of all Android</a> users on it.
</p>

<p>
I ended up using a ROM image from <a href="http://android.modaco.com/content/google-nexus-one-nexusone-modaco-com/317849/22-oct-r24-modaco-custom-rom-desire-port-for-nexus-one-with-online-kitchen-2-2-froyo/" title="Modaco" target="_blank">modaco</a> for the nexus one (note: link may require registration).
</p>

<p>
So here’s how it all comes together (note, I am using Windows below, but it’s nearly identical under Mac or Linux):
</p>

<ol>
	<li>Create an Android 2.2 AVD</li>
	<li><p>Copy the system.img that comes with the Android SDK to your new AVD folder. ex:</p>
<pre>
D:\android-sdk-windows\platforms\android-8\images\system.img
to
C:\Users\drodger\.android\avd\AndMarket22.avd\
</pre></li>
	<li><p>Now you’ll need to start the emulator, but you need to tell it how much internal storage to use (the default isn’t enough). In the AVD manager, select the New… button by the Hardware section, and scroll down and select the Device ram size property, and then edit the value to 128 (just click on the value). Here’s the command line version:</p>
	<pre>D:\android-sdk-windows\tools\emulator -avd AndMarket22.avd -partition-size 128</pre></li>
	<li>Wait. Wait some more. The emulator is slow to load this one up sometimes. Don’t bother with the next step until the emulator has completely started.</li>
	<li>Now you need to get the build.prop file from within the emulator image, and make a change, and push the change back, like so:
	<pre>D:\android-sdk-windows\tools\adb pull /system/build.prop</pre></li>
	<li>Now edit that file (it will now be in your tools\ directory), and comment out the following line by putting a '#' at the beginning of the line:
<pre>
ro.config.nocheckin=yes
#ro.config.nocheckin=yes
</pre></li>
	<li>Now you need to push it back:<pre>D:\android-sdk-windows\tools\adb remount</pre></li>
	<li><pre>D:\android-sdk-windows\tools\adb push build.prop /system/build.prop</pre></li>
	<li>Now you need the ROM you downloaded from modaco</li>
	<li>Look within the zip, in the \system\app folder</li>
	<li>Copy GoogleServicesFramework.apk and Vending.apk to your tools\ directory.</li>
	<li><pre>D:\android-sdk-windows\tools\adb push GoogleServicesFramework.apk /system/app</pre></li>
	<li><pre>D:\android-sdk-windows\tools\adb push Vending.apk /system.app</pre></li>
	<li>Remove the SDK setup package:</li>
	<li><pre>D:\android-sdk-windows\tools\adb shell rm /system/app/SdkSetup.apk</pre></li>
	<li>Close the emulator</li>
	<li>Delete these files in your AVD directory: cache.img, userdata.img, userdata-qemu.img</li>
	<li>Ok, now go start the emulator again, and you should be good to go!</li>
</ol>

<img alt="emulator" src="http://dl.dropbox.com/u/7133191/Capture.jpg"/>
