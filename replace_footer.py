from pathlib import Path

root = Path(__file__).parent
replace_old = 'Designed by <a href="https://bootstrapmade.com/">BootstrapMade</a>. Distributed by <a href="https://themewagon.com" target="_blank">ThemeWagon</a>'
replace_new = 'Developed by <a href="https://github.com/syedmushtaq4033">Syed Mushtaq</a> • GitHub: <a href="https://github.com/syedmushtaq4033">syedmushtaq4033</a>'
updated = 0
for html in root.glob('*.html'):
    text = html.read_text(encoding='utf-8')
    if replace_old in text:
        html.write_text(text.replace(replace_old, replace_new), encoding='utf-8')
        updated += 1
print(f'Updated {updated} HTML files.')

readme_txt = root / 'Readme.txt'
if readme_txt.exists():
    content = readme_txt.read_text(encoding='utf-8')
    readme_md = root / 'README.md'
    readme_md.write_text(content, encoding='utf-8')
    print('Created README.md from Readme.txt.')
