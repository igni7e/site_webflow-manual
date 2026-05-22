from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path
import textwrap


ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "src" / "assets" / "diagrams" / "manual"
DOCS_DIR = ROOT / "src" / "content" / "docs"
INVENTORY = ROOT / "docs" / "diagram-inventory-2026-05-22.md"
REL_ASSET_PREFIX = "../../../assets/diagrams/manual"


@dataclass(frozen=True)
class Diagram:
    id: str
    title: str
    subtitle: str
    page: str
    section: str
    boxes: tuple[str, ...]
    note: str
    color: str

    @property
    def filename(self) -> str:
        return f"{self.id}-{slugify(self.title)}.svg"


def slugify(text: str) -> str:
    table = {
        "Workspace": "workspace",
        "Site": "site",
        "Plan": "plan",
        "Content": "content",
        "Editor": "editor",
        "Designer": "designer",
        "CMS": "cms",
        "Publish": "publish",
        "Domain": "domain",
        "SEO": "seo",
        "Locale": "locale",
        "Form": "form",
        "Trouble": "trouble",
    }
    out = []
    ascii_mode = False
    for ch in text:
        if ch.isascii() and ch.isalnum():
            out.append(ch.lower())
            ascii_mode = True
        elif ch in "-_ ":
            out.append("-")
            ascii_mode = False
        elif ascii_mode:
            out.append("-")
            ascii_mode = False
    slug = "".join(out).strip("-")
    for src, dst in table.items():
        if src.lower() in text.lower() and dst not in slug:
            slug = f"{dst}-{slug}" if slug else dst
    return "-".join(part for part in slug.split("-") if part) or "diagram"


DIAGRAMS: list[Diagram] = [
    Diagram("diagram-01", "WorkspaceとSiteの親子関係", "まずWorkspaceがあり、その中に複数のSiteがあります。", "01-getting-started/00-workspace-intro.md", "Workspaceの基本構造", ("Workspace", "Site A", "Site B", "Members"), "Workspaceは会社やチームの入れ物。Siteはその中の1つのWebサイトです。", "#315C8A"),
    Diagram("diagram-02", "Workspace planとSite planの違い", "料金や権限の話で混同しやすい2つを分けます。", "01-getting-started/00-plan-role-decision.md", "Plan判断", ("Workspace plan", "メンバー管理", "Site plan", "公開・CMS容量"), "Workspace planはチーム側、Site planはサイト公開側の契約です。", "#596B2D"),
    Diagram("diagram-03", "誰をどこに追加するか", "メンバー追加はWorkspace側とSite側の影響を分けて考えます。", "01-getting-started/00-add-member.md", "メンバー追加", ("招待する人", "Workspace role", "Site role", "Can publish"), "招待前に、何をしてほしい人なのかを先に決めます。", "#6B4E71"),
    Diagram("diagram-04", "Dashboardから開く入口", "Open in Webflow、Settings、Designerを押し間違えないための整理です。", "01-getting-started/00-open-site.md", "Dashboard入口", ("Dashboard", "Open in Webflow", "Settings", "Designer"), "日常更新はOpen in Webflowから入り、Designerは必要な時だけ使います。", "#7B4D2A"),
    Diagram("diagram-05", "Workspace planで見る項目", "メンバー数、権限、チーム管理を見る場所です。", "01-getting-started/00-workspace-plan.md", "Workspace plan", ("Plan名", "Seats", "Members", "Roles"), "サイト公開の有無ではなく、チームとして使える範囲を確認します。", "#285A4D"),
    Diagram("diagram-06", "Site planで見る項目", "CMS、フォーム、公開先ドメインなど、サイト単位の範囲です。", "01-getting-started/00-site-plan.md", "Site plan", ("Hosting", "CMS", "Forms", "Bandwidth"), "公開サイトに必要な機能はSite plan側で確認します。", "#8A4B5B"),
    Diagram("diagram-07", "通常更新の安全ルート", "迷った時はContent editor roleから始めます。", "01-getting-started/08-editor-only-recommendation.md", "安全な入口", ("Dashboard", "Content editor role", "文字・画像・CMS", "Publish確認"), "デザインや構造を触らず、公開前チェックまで進めるのが基本です。", "#2F5F73"),
    Diagram("diagram-08", "EditorとDesignerの境界", "触ってよい範囲と止める範囲を分けます。", "01-getting-started/07-editor-vs-designer.md", "Editor vs Designer", ("Editor", "内容更新", "Designer", "構造・見た目"), "文章や画像はEditor、レイアウト変更はDesignerです。", "#784F7A"),
    Diagram("diagram-09", "初回ログイン後の確認順", "入ってすぐ押す前に、サイト名と権限を確認します。", "01-getting-started/11-after-login-first-steps.md", "初回確認", ("ログイン", "Workspace確認", "Site確認", "入口確認"), "最初に正しいWorkspaceとSiteにいるか見ます。", "#526D33"),
    Diagram("diagram-10", "Webflow用語のつながり", "英語UIで迷いやすい言葉の関係図です。", "01-getting-started/10-webflow-ui-glossary.md", "用語整理", ("Workspace", "Site", "CMS", "Publish"), "単語を単体で覚えるより、どこで使う言葉かで覚えます。", "#A05A36"),
    Diagram("diagram-11", "Content Editorで開く流れ", "最新版Content editor roleで開くまでの流れです。", "02-editor/02-open-content-editor.md", "開き方", ("Dashboard", "Open in Webflow", "Canvas", "編集対象"), "開いたらすぐ編集せず、ページと権限を確認します。", "#315C8A"),
    Diagram("diagram-12", "編集アイコンが出る条件", "編集できる要素とできない要素を見分けます。", "02-editor/13-latest-content-editor-screen-guide.md", "画面の見方", ("ログイン", "権限", "編集可能要素", "アイコン表示"), "アイコンが出ない時は、権限か対象要素を確認します。", "#596B2D"),
    Diagram("diagram-13", "テキスト修正の安全手順", "文章を変える時の基本フローです。", "02-editor/03-edit-text.md", "テキスト編集", ("選択", "編集", "確認", "Publish"), "長文は先に下書きしてから貼り付けると安全です。", "#6B4E71"),
    Diagram("diagram-14", "画像差し替えの判断", "画像を変える前にサイズ・権利・表示を確認します。", "02-editor/06-replace-image.md", "画像差し替え", ("画像選択", "Upload", "表示確認", "スマホ確認"), "差し替え後は縦横比とスマホ表示を必ず見ます。", "#7B4D2A"),
    Diagram("diagram-15", "リンク変更の確認範囲", "URLだけでなく開き方も確認します。", "02-editor/07-edit-link-url.md", "リンク変更", ("リンク選択", "URL確認", "新規タブ", "クリック確認"), "外部リンクは必要に応じて新しいタブにします。", "#285A4D"),
    Diagram("diagram-16", "Publish前の判断", "公開してよい変更かを確認してから押します。", "02-editor/12-before-publish-checklist.md", "公開前確認", ("変更内容", "公開先", "スマホ", "リンク"), "Publishは公開操作です。迷ったら止めます。", "#8A4B5B"),
    Diagram("diagram-17", "Publishの流れ", "保存と公開の違いを分けます。", "02-editor/08-save-and-publish.md", "Publish", ("編集", "保存", "公開先確認", "公開サイト確認"), "公開後は必ず実サイトで確認します。", "#2F5F73"),
    Diagram("diagram-18", "変更破棄の考え方", "Discardは戻せない場合があるため慎重に扱います。", "02-editor/09-discard-changes.md", "変更破棄", ("未公開変更", "内容確認", "Discard", "再確認"), "捨ててよい変更か分からない時は実行しません。", "#784F7A"),
    Diagram("diagram-19", "CMSの全体像", "CMSは同じ形式の記事を管理する仕組みです。", "03-cms/00-blog-post-complete-guide.md", "CMS概要", ("Collection", "Item", "Fields", "Template"), "記事一覧と記事詳細はCMS itemから作られます。", "#526D33"),
    Diagram("diagram-20", "CMS item作成フロー", "新規記事を作る時の流れです。", "03-cms/02-create-new-post.md", "新規記事", ("Collection", "New item", "Fields入力", "Draft/Publish"), "まず下書き保存し、公開前に確認します。", "#A05A36"),
    Diagram("diagram-21", "TitleとSlugの関係", "タイトルは表示名、SlugはURLです。", "03-cms/03-post-title.md", "Title/Slug", ("Title", "Slug", "URL", "公開後確認"), "Slugは公開後に変えるとURLが変わります。", "#315C8A"),
    Diagram("diagram-22", "サムネイルと本文画像", "画像が表示される場所を分けて理解します。", "03-cms/04-thumbnail-image.md", "画像Field", ("Thumbnail", "一覧", "本文画像", "詳細ページ"), "一覧用画像と本文中画像は別のFieldの場合があります。", "#596B2D"),
    Diagram("diagram-23", "カテゴリー選択の影響", "カテゴリーは一覧や絞り込みに影響します。", "03-cms/05-post-category.md", "カテゴリー", ("Category", "一覧表示", "絞り込み", "関連記事"), "違うカテゴリーを選ぶと出る場所が変わる場合があります。", "#6B4E71"),
    Diagram("diagram-24", "Rich Text本文の構造", "本文は見出し、段落、画像、リンクで構成します。", "03-cms/06-write-body.md", "本文", ("見出し", "段落", "画像", "リンク"), "見出しの順番を崩さず、読みやすく整えます。", "#7B4D2A"),
    Diagram("diagram-25", "下書きから公開まで", "Draft、Scheduled、Publishedの違いです。", "03-cms/16-save-as-draft.md", "公開状態", ("Draft", "Review", "Schedule", "Published"), "今どの状態かを確認してから操作します。", "#285A4D"),
    Diagram("diagram-26", "公開済み記事の修正", "公開済み記事は保存が公開に近い意味になる場合があります。", "03-cms/18-edit-published.md", "公開済み修正", ("Published", "Edit", "Save", "Live確認"), "公開済み記事は変更後の反映タイミングに注意します。", "#8A4B5B"),
    Diagram("diagram-27", "非公開・アーカイブ・削除", "似ている操作でも影響が違います。", "03-cms/19-unpublish.md", "非公開", ("Unpublish", "Archive", "Delete", "Restore相談"), "削除は最終手段。迷ったらArchiveや相談を優先します。", "#2F5F73"),
    Diagram("diagram-28", "CMS公開前チェック", "公開前に見る場所をまとめます。", "03-cms/25-cms-before-publish-checklist.md", "公開前", ("詳細ページ", "一覧", "スマホ", "SNS表示"), "記事は複数箇所に出るため、一覧も確認します。", "#784F7A"),
    Diagram("diagram-29", "Morbido Fieldの見方", "入力Fieldは表示場所と対応しています。", "03-cms/26-morbido-cms-field-guide.md", "Morbido Fields", ("Title", "Summary", "Thumbnail", "Body"), "どこに表示されるFieldか確認してから入力します。", "#526D33"),
    Diagram("diagram-30", "本文リンクと外部リンク", "本文中リンクは公開後クリック確認します。", "03-cms/13-body-link.md", "本文リンク", ("文字選択", "リンク設定", "新規タブ", "クリック確認"), "リンク切れは公開前に必ず潰します。", "#A05A36"),
    Diagram("diagram-31", "Designerを開く前の判断", "Designerは最終手段として扱います。", "04-designer/01-designer-warning.md", "Designer注意", ("目的確認", "バックアップ", "対象だけ編集", "相談"), "目的が曖昧なら開かない方が安全です。", "#315C8A"),
    Diagram("diagram-32", "Designer画面の三層", "左、中央、右の役割を分けます。", "04-designer/02-edit-homepage-text.md", "Designer画面", ("Navigator", "Canvas", "Style panel", "Publish"), "中央だけでなく左右の設定にも影響が出ます。", "#596B2D"),
    Diagram("diagram-33", "Asset Panelの考え方", "画像やファイルはAssetsで管理されます。", "04-designer/05-asset-panel.md", "Assets", ("Upload", "Asset", "利用箇所", "削除注意"), "使われているAssetを消すと表示崩れにつながります。", "#6B4E71"),
    Diagram("diagram-34", "Undoと復元の違い", "作業中のUndoとBackup復元は別物です。", "04-designer/08-undo-ctrl-z.md", "Undo", ("Undo", "保存前", "Backup", "復元依頼"), "大きく戻す場合はBackup確認が必要です。", "#7B4D2A"),
    Diagram("diagram-35", "SEO titleの位置づけ", "検索結果とブラウザタブに関わります。", "05-settings/01-seo-title.md", "SEO title", ("Page", "Title tag", "検索結果", "クリック"), "短く、分かりやすく、重要語を前に置きます。", "#285A4D"),
    Diagram("diagram-36", "Meta descriptionの役割", "検索結果の説明文として使われることがあります。", "05-settings/02-seo-description.md", "Meta description", ("ページ内容", "説明文", "検索結果", "反映待ち"), "すぐ反映されないため、公開確認と検索確認を分けます。", "#8A4B5B"),
    Diagram("diagram-37", "OGP画像の表示先", "SNS共有時の見え方に影響します。", "05-settings/03-ogp-image.md", "OGP", ("OGP image", "SNS", "共有プレビュー", "再取得"), "SNS側のキャッシュで古い画像が残る場合があります。", "#2F5F73"),
    Diagram("diagram-38", "Forms確認の流れ", "フォーム送信はWebflow上の記録と通知メールを分けます。", "05-settings/04-form-submissions.md", "Forms", ("Form", "Submission", "CSV", "通知メール"), "メールが届かなくてもSubmissionに残っている場合があります。", "#784F7A"),
    Diagram("diagram-39", "CSVダウンロードの注意", "個人情報を含むため扱いに注意します。", "05-settings/06-form-csv-download.md", "CSV", ("Submissions", "Export CSV", "保存先", "削除/共有注意"), "CSVは個人情報ファイルとして扱います。", "#526D33"),
    Diagram("diagram-40", "DomainとSSLの関係", "ドメイン接続と鍵マークは別々に確認します。", "05-settings/09-domain-status.md", "Domain/SSL", ("Domain", "DNS", "Connected", "SSL Active"), "ConnectedでもSSL Pendingのことがあります。", "#A05A36"),
    Diagram("diagram-41", "sitemapとnoindex", "検索に出す・出さないを分けます。", "05-settings/10-search-engine-control.md", "SEO制御", ("sitemap", "noindex", "Publish", "検索反映"), "noindex解除忘れは重大なので必ず記録します。", "#315C8A"),
    Diagram("diagram-42", "Locale翻訳の流れ", "Locale選択から公開までを順番に進めます。", "07-localization/00-localization-overview.md", "Locale概要", ("Locale選択", "翻訳", "SEO確認", "Publish"), "今どのLocaleを触っているかを最初に確認します。", "#596B2D"),
    Diagram("diagram-43", "PrimaryとSecondary Locale", "基準言語と追加言語を分けます。", "07-localization/06-add-new-locale.md", "Locale追加", ("Primary", "Secondary", "URL", "Publishing"), "Primary localeは後から簡単に変えられません。", "#6B4E71"),
    Diagram("diagram-44", "静的ページ翻訳", "ページ上のテキスト、リンク、画像を確認します。", "07-localization/02-static-page-translation.md", "静的ページ", ("ページ選択", "テキスト", "リンク", "スマホ確認"), "翻訳後は長さで崩れやすくなります。", "#7B4D2A"),
    Diagram("diagram-45", "CMS Locale翻訳", "CMS itemもLocaleごとに確認します。", "07-localization/03-cms-locale-translation.md", "CMS翻訳", ("CMS item", "Locale", "Title/Body", "一覧確認"), "一覧と詳細の両方で翻訳表示を見ます。", "#285A4D"),
    Diagram("diagram-46", "Locale SEO/OGP", "言語ごとの検索・SNS表示を確認します。", "07-localization/04-localized-seo-ogp.md", "Locale SEO", ("Title", "Description", "OGP", "Slug"), "各LocaleでSEO文言が自然か確認します。", "#8A4B5B"),
    Diagram("diagram-47", "変更が反映されない時", "原因を4つに分けて切り分けます。", "06-troubleshooting/01-cache-not-reflecting.md", "反映されない", ("Publish", "Cache", "Domain", "CMS status"), "まずPublishと公開先を確認します。", "#2F5F73"),
    Diagram("diagram-48", "画像アップロード失敗", "ファイル側、通信側、権限側に分けます。", "06-troubleshooting/02-image-upload-failed.md", "画像トラブル", ("形式", "容量", "通信", "権限"), "原因を分けると相談が早くなります。", "#784F7A"),
    Diagram("diagram-49", "404の原因整理", "URL、Slug、公開状態を確認します。", "06-troubleshooting/04-404-not-found.md", "404", ("URL", "Slug", "Published", "Redirect相談"), "Slug変更後は古いURLが404になることがあります。", "#526D33"),
    Diagram("diagram-50", "保守依頼に必要な情報", "相談時に送ると早い情報です。", "06-troubleshooting/07-maintenance-request.md", "保守依頼", ("URL", "現象", "操作", "スクショ"), "スクショとURLがあると原因確認がかなり早くなります。", "#A05A36"),
]


def wrap_svg_text(text: str, width: int = 18) -> list[str]:
    lines: list[str] = []
    current = ""
    units = 0
    for ch in text:
        weight = 1 if ch.isascii() else 2
        if units + weight > width and current:
            lines.append(current)
            current = ch
            units = weight
        else:
            current += ch
            units += weight
    if current:
        lines.append(current)
    return lines[:4]


def svg_text(x: int, y: int, text: str, size: int, color: str = "#172033", weight: str = "500", anchor: str = "start") -> str:
    return f'<text x="{x}" y="{y}" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{escape(text)}</text>'


def color_mix(hex_color: str, target: str = "#FFFFFF", ratio: float = 0.86) -> str:
    src = hex_color.lstrip("#")
    dst = target.lstrip("#")
    sr, sg, sb = int(src[0:2], 16), int(src[2:4], 16), int(src[4:6], 16)
    tr, tg, tb = int(dst[0:2], 16), int(dst[2:4], 16), int(dst[4:6], 16)
    r = round(sr * (1 - ratio) + tr * ratio)
    g = round(sg * (1 - ratio) + tg * ratio)
    b = round(sb * (1 - ratio) + tb * ratio)
    return f"#{r:02X}{g:02X}{b:02X}"


def draw_box(x: int, y: int, w: int, h: int, label: str, color: str, idx: int) -> str:
    tint = color_mix(color, "#FFFFFF", 0.94)
    parts = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#ffffff" stroke="#CBD5E1" stroke-width="2"/>',
        f'<rect x="{x}" y="{y}" width="6" height="{h}" rx="3" fill="{color}"/>',
        f'<circle cx="{x + 34}" cy="{y + 34}" r="15" fill="{tint}" stroke="{color}" stroke-width="2"/>',
        svg_text(x + 34, y + 40, str(idx), 15, color, "800", "middle"),
    ]
    for i, line in enumerate(wrap_svg_text(label, 16)):
        parts.append(svg_text(x + 62, y + 34 + i * 23, line, 22, "#172033", "700"))
    return "\n".join(parts)


def draw_arrow(x1: int, y: int, x2: int, color: str) -> str:
    return "\n".join(
        [
            f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color}" stroke-width="4" stroke-linecap="round"/>',
            f'<path d="M {x2 - 14} {y - 10} L {x2} {y} L {x2 - 14} {y + 10}" fill="none" stroke="{color}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>',
        ]
    )


def render_svg(diagram: Diagram) -> str:
    bg = "#FFFFFF"
    muted = "#5F6B7A"
    color = diagram.color
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="420" viewBox="0 0 1120 420" role="img">',
        f"<title>{escape(diagram.title)}</title>",
        f"<desc>{escape(diagram.subtitle)}</desc>",
        f'<rect width="1120" height="420" fill="{bg}"/>',
        f'<rect x="28" y="28" width="1064" height="364" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2"/>',
        svg_text(56, 76, diagram.title, 28, "#172033", "800"),
        svg_text(58, 108, diagram.subtitle, 18, muted, "500"),
    ]

    box_count = len(diagram.boxes)
    gap = 24
    box_w = int((1008 - gap * (box_count - 1)) / box_count)
    box_h = 112
    start_x = 56
    y = 156
    for idx, label in enumerate(diagram.boxes, start=1):
        x = start_x + (idx - 1) * (box_w + gap)
        parts.append(draw_box(x, y, box_w, box_h, label, color, idx))
        if idx < box_count:
            parts.append(draw_arrow(x + box_w + 4, y + box_h // 2, x + box_w + gap - 4, color))

    parts.extend(
        [
            f'<line x1="56" y1="306" x2="1064" y2="306" stroke="#E2E8F0" stroke-width="2"/>',
            f'<circle cx="70" cy="346" r="6" fill="{color}"/>',
        ]
    )
    wrapped_note = textwrap.wrap(diagram.note, width=54)
    for i, line in enumerate(wrapped_note[:2]):
        parts.append(svg_text(90, 352 + i * 22, line, 18, "#172033", "600"))
    parts.append("</svg>")
    return "\n".join(parts)


def insert_diagram(page: Path, diagram: Diagram) -> bool:
    text = page.read_text()
    if diagram.filename in text:
        return False
    lines = text.splitlines()
    insert_at = None
    for i, line in enumerate(lines):
        if line.startswith("# "):
            insert_at = i + 1
            break
    if insert_at is None:
        insert_at = len(lines)
    alt = f"{diagram.title}の図解"
    block = [
        "",
        f"![{alt}]({REL_ASSET_PREFIX}/{diagram.filename})",
        "",
        f":::note[図解の見方]",
        f"{diagram.note}",
        ":::",
        "",
    ]
    lines[insert_at:insert_at] = block
    page.write_text("\n".join(lines) + "\n")
    return True


def write_inventory() -> None:
    rows = [
        "---",
        'title: "Python生成図解一覧 2026-05-22"',
        'description: "Webflowマニュアルに追加したPython生成図解50枚のファイル名、差し込み先、用途の一覧。"',
        "---",
        "",
        "# Python生成図解一覧 2026-05-22",
        "",
        "Pythonで生成したSVG図解を `src/assets/diagrams/manual/` に保存し、各本文ページへ差し込みました。",
        "",
        "| ID | ファイル | 差し込み先 | 用途 |",
        "| --- | --- | --- | --- |",
    ]
    for d in DIAGRAMS:
        rows.append(f"| {d.id} | `{d.filename}` | `{d.page}` | {d.section} |")
    INVENTORY.write_text("\n".join(rows) + "\n")


def main() -> None:
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    generated = 0
    inserted = 0
    for diagram in DIAGRAMS:
        (ASSET_DIR / diagram.filename).write_text(render_svg(diagram))
        generated += 1
        page = DOCS_DIR / diagram.page
        if not page.exists():
            raise FileNotFoundError(page)
        if insert_diagram(page, diagram):
            inserted += 1
    write_inventory()
    print(f"generated={generated} inserted={inserted} inventory={INVENTORY.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
