---
presentation:
  controls: true
  controlsLayout: 'edges'
  slideNumber: true
  history: true
  keyboard: true
  autoSlide: 0
  autoSlideStoppable: true
  mouseWheel: true
  transitionSpeed: 'fast'
  backgroundTransition: 'concave'
  enableSpeakerNotes:  true
---

<!-- slide -->
# Markdownでプレゼンテーション作成
# サンプル

~ by b1tblog ~

<!-- slide -->
## プロパティを設定しよう

```markdown
---
presentation:
  width: 800
  height: 600
---
```

<!-- slide -->
## スライドを追加しよう

```markdown
<!-- slide -->
初めてのスライド
```

<!-- slide -->
## スライドはMarkdownで書こう


```markdown
<!-- slide -->
$$ f(x) = x^2 + 1$$
```
$$ f(x) = x^2 + 1$$

<p class="fragment highlight-red">シンタックスハイライトや数式はそのまま使えるよ</p>

<!-- slide data-background-color="#273c75" -->
## 背景色を設定しよう


```markdown
<!-- slide data-background-color="#273c75" -->
## 背景色を設定しよう
```

<!-- slide data-background-image="https://b1tblog.com/wp-content/uploads/2019/09/vscode.png" -->
<h2 style="color:#44bd32">背景画像を設定しよう</h2>

```markdown
<!-- slide data-background-image="https://b1tblog.com/wp-content/uploads/2019/09/vscode.png" -->
## 背景画像を設定しよう
```

<!-- slide data-transition="fade" -->
## アニメーションを設定しよう

```markdown
<!-- slide data-transition="fade" -->
```

<!-- slide data-transition="fade" -->
## 下移動を追加しよう
**↓下に移動して確認してね**

<!-- slide vertical=true -->
## 下移動
```markdown
<!-- slide vertical=true -->
```

<!-- slide -->
## 要素のアニメーションを設定しよう

```markdown
- Item 1 <!-- .element: class="fragment shrink" data-fragment-index="2" -->
- Item 2 <!-- .element: class="fragment" data-fragment-index="1" -->
```
- Item 1 <!-- .element: class="fragment shrink" data-fragment-index="2" -->
- Item 2 <!-- .element: class="fragment" data-fragment-index="1" -->

<!-- slide -->
## スピーカーノートを設定しよう

```markdown
---
presentation:
  enableSpeakerNotes: true
---
```

<!-- slide vertical=true -->
```markdown
<!-- slide data-notes="ノートを追加したよ" -->
```

<!-- slide vertical=true data-notes="ノートを追加したよ"-->
**Sキーを押して確認してね**

<!-- slide -->
## おしまい








