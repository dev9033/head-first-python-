# gives html encoded text
import html

print(html.escape("this html fragment contains a <script>script</script> tag."))

print(html.unescape("I &hearts; Python's &lt;standard library&gt;."))
