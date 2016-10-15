from AppKit import NSSpeechSynthesizer
speechSynthesizer = NSSpeechSynthesizer.alloc().initWithVoice_("com.apple.speech.synthesis.voice.Bruce")
print "hello"
speechSynthesizer.startSpeakingString_('Hi! Nice to meet you!')