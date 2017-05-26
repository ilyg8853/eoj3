var map = {
  'c': 'c_cpp',
  'c11': 'c_cpp',
  'cpp98': 'c_cpp',
  'cpp': 'c_cpp',
  'cpp14': 'c_cpp',
  'csharp': 'csharp',
  'python2': 'python',
  'python': 'python',
  'java': 'java',
  'php': 'php',
  'fortran': 'fortran',
  'perl': 'perl',
  'ruby': 'ruby',
  'objc': 'objectivec',
  'haskell': 'haskell',
  'scala': 'scala',
  'lua': 'lua',
  'lisp': 'lisp',
  'js': 'javascript',
  'go': 'golang',
  'ocaml': 'ocaml',
  'fsharp': 'text',
  'pypy2': 'python',
  'swift': 'swift',
  'pascal': 'pascal',
  'rust': 'rust',
  'r': 'r'
};
var editor = ace.edit("editor");
var lang = $("#id_lang");
var code = $("#id_code");
editor.getSession().setValue(code.val());
editor.setTheme("ace/theme/chrome");
editor.getSession().setMode("ace/mode/" + map[lang.val()]);
lang.on("change", function (event) {
  editor.getSession().setMode("ace/mode/" + map[event.target.value]);
});
function setVal() {
  code.val(editor.getSession().getValue())
}
$('form').submit(function () {
  $(this).find('button[type=submit]').prop('disabled', true);
});