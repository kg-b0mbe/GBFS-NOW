# CHANGELOG

## [Unreleased] — QGIS 3.38 対応

### 背景

QGIS 3.38 は Qt 6 ベースに移行し、PyQt5 の一部 API が非推奨・廃止になりました。
本 PR はその変更に追従し、**QGIS 3.38 以降でも動作**しつつ、**3.38 未満との後方互換**を保ちます。

---

### 新規追加

#### `compat.py`（新規ファイル）

QGIS バージョンによって型定数と列挙値を切り替えるヘルパーモジュールを追加しました。

```python
# QGIS 3.38+ では QMetaType.Type.* を使用
# QGIS 3.38 未満では QVariant.* を使用
if Qgis.versionInt() >= 33800:
    FIELD_STRING = QMetaType.Type.QString
    ...
    DIALOG_ACCEPTED = QDialog.DialogCode.Accepted
else:
    FIELD_STRING = QVariant.String
    ...
    DIALOG_ACCEPTED = QDialog.Accepted
```

各ファイルはこのモジュールから定数を import するだけで、バージョン分岐を意識せずに済みます。

---

### 変更

#### `gbfs_now_stations.py`

| 変更前 | 変更後 |
|--------|--------|
| `from qgis.PyQt.QtCore import QVariant` | `from .compat import FIELD_STRING, FIELD_INT, FIELD_DOUBLE, FIELD_BOOL` |
| `QVariant.String` | `FIELD_STRING` |
| `QVariant.Int` | `FIELD_INT` |
| `QVariant.Double` | `FIELD_DOUBLE` |
| `QVariant.Bool` | `FIELD_BOOL` |

`QgsField()` の型指定を全箇所（英語版・日本語版の両関数）で置き換えました。

#### `gbfs_now_stations_status.py`

`gbfs_now_stations.py` と同様に `QVariant.*` を `compat.py` 経由の定数に置き換えました。

#### `gbfs_now_free_bike_status.py`

`gbfs_now_stations.py` と同様に `QVariant.*` を `compat.py` 経由の定数に置き換えました。

#### `gbfs_now_vehicle_types.py`

`QgsField` の定義はありませんでしたが、使用されていない `QVariant` の import を除去しました。

#### `gbfs_now_search_dialog.py`

1. **CSVカラム名のハードコードを廃止**
   - `systems.csv` のカラム名をコード内に直書きしていたのをやめ、
     `df.columns.tolist()` で取得したカラム名を `createTableModel()` に渡すようにしました。
   - MobilityData がカラム名を変更しても、コード修正なしに追従できます。

2. **`QDialog.Accepted` → `DIALOG_ACCEPTED`（compat 経由）**
   - Qt 6 では `QDialog.Accepted` が `QDialog.DialogCode.Accepted` に変わりました。
   - `compat.py` の `DIALOG_ACCEPTED` を使うことで、新旧 QGIS 両方で動作します。

3. **不要な `QVariant` import を除去**

---

### 修正ファイル一覧

```
GBFS-NOW/
├── compat.py                    ← 新規追加
├── gbfs_now_stations.py         ← QVariant → compat 定数
├── gbfs_now_stations_status.py  ← QVariant → compat 定数
├── gbfs_now_free_bike_status.py ← QVariant → compat 定数
├── gbfs_now_vehicle_types.py    ← 不要 QVariant import 除去
└── gbfs_now_search_dialog.py    ← CSVカラム動的取得 / QDialog.Accepted 修正
```

---

### 動作確認バージョン

| QGIS バージョン | Qt バージョン | 動作 |
|----------------|-------------|------|
| 3.38 以降       | Qt 6         | ✅   |
| 3.38 未満       | Qt 5         | ✅（後方互換）|
