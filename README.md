<!DOCTYPE html>
<html>
<head>

<style>
#typing-text {
	width: 530px;
	height: 47px;
	font-size: 15px;
	border: solid 2px #db0909;
	color: #080202;
	background-color: #09b3d9;
	text-align: center;
	font-family: Arial;
	overflow: hidden;
	font-weight: bold;
	padding: 5px;
	resize: none;
	outline: none;
	box-sizing: border-box;
}
</style>
</head>
<body>
<textarea id="typing-text" readonly></textarea>

<script>
(() => {
	let TypingSpeed = 50;
	let NxtMsgDelay = 1000;
	let CharacterPos = 0;
	let MsgBuffer = "";
	let MsgIndex = 0;
	let delay;
	let id = document.getElementById("typing-text");
	let messages =
[
	"Welcome to our Higher Languages Programming repository on GitHub!\n\nWe're thrilled to have you here, where the world of programming languages reaches new heights. This repository is dedicated to exploring and developing advanced programming languages that push the boundaries of what's possible in software development.\n\nWhether you're a seasoned programmer or just starting your coding journey, this repository is a treasure trove of knowledge, innovation, and collaboration. You'll find a wealth of resources, tools, and cutting-edge research that will broaden your understanding of high-level programming languages.\n\nFeel free to dive in, explore the code, contribute your own creations, and engage with fellow developers. We believe in the power of community and open collaboration, where diverse minds converge to shape the future of programming.\n\nFrom functional programming to domain-specific languages, from compiler design to advanced type systems, we cover a wide range of topics that will challenge and inspire you. Expect to encounter fascinating discussions, insightful code snippets, and thought-provoking projects that will elevate your programming skills to new heights.\n\nRemember, this is not just a repository; it's a platform for learning, sharing ideas, and fostering innovation. Together, we can push the boundaries of what programming languages can achieve and unlock new possibilities for software development.\n\nJoin us on this exciting journey and be part of the revolution in higher languages programming. Your contributions, ideas, and enthusiasm will shape the future of this repository and the programming world at large.\n\nOnce again, welcome to our Higher Languages Programming repository. Happy coding!\n\nBest regards,\n[Your Name]"
]

	// https://www.html-code-generator.com/html/typewriter-text-scroller
	const StartTyping = () => {
		if (CharacterPos != messages[MsgIndex].length) {
			MsgBuffer += messages[MsgIndex].charAt(CharacterPos);
			id.value = MsgBuffer+(CharacterPos != messages[MsgIndex].length-1 ? "_":"");
			delay = TypingSpeed;
			id.scrollTop = id.scrollHeight; 
		} else {
			delay = NxtMsgDelay;
			MsgBuffer   = "";
			CharacterPos = -1;
			if (MsgIndex!= messages.length-1){
				MsgIndex++;
			}else {
				MsgIndex = 0;
			}
		}
		CharacterPos++;
		setTimeout(StartTyping, delay);
	}
	StartTyping();
})();

</script>

</body>
</html>
