# Từ vựng component + mapping ARIA — wireframe-docs

> Nguồn sự thật cho `Kiểu` trong tree và mapping ngữ nghĩa cho `check-guidelines.py`.
> Danh sách shadcn pin từ `ui.shadcn.com/docs/components` (mục All Components),
> đối chiếu ngày 03/11/2026. Mapping role đối chiếu MDN ARIA Roles
> (dựa trên W3C WAI-ARIA, trang sửa đổi 14/10/2026, truy cập 03/11/2026).

## Danh sách shadcn pin (66 mục, PascalCase trong tree)

Accordion, Alert, AlertDialog, AspectRatio, Attachment, Avatar, Badge,
Breadcrumb, Bubble, Button, ButtonGroup, Calendar, Card, Carousel, Chart,
Checkbox, CodeBlock, Collapsible, Combobox, Command, ContextMenu, DataTable,
DatePicker, Dialog, Direction, Drawer, DropdownMenu, Empty, Field, HoverCard,
Input, InputGroup, InputOTP, Item, Kbd, Label, Marker, Menubar, Message,
MessageScroller, NativeSelect, NavigationMenu, Pagination, Popover, Progress,
Questionnaire, RadioGroup, Resizable, ScrollArea, Select, Separator, Sheet,
Sidebar, Skeleton, Slider, Spinner, Switch, Table, Tabs, Textarea, Toast,
Toggle, ToggleGroup, Tooltip, Trace, Typography.

Không thuộc AI Elements (Chat, PromptInput... — ngoài phạm vi v1).
shadcn ra component mới → bổ sung tên + mapping cùng commit (luật mở rộng).

## Layout primitives (repo tự định nghĩa, 4 mục)

Section, Grid, Stack, Container — dùng cho khung chứa trong wireframe;
không thay thế component shadcn.

## Khối máy đọc (check.py parse — cấm sửa tay sai định dạng)

```type-vocab
Accordion
Alert
AlertDialog
AspectRatio
Attachment
Avatar
Badge
Breadcrumb
Bubble
Button
ButtonGroup
Calendar
Card
Carousel
Chart
Checkbox
CodeBlock
Collapsible
Combobox
Command
ContextMenu
DataTable
DatePicker
Dialog
Direction
Drawer
DropdownMenu
Empty
Field
HoverCard
Input
InputGroup
InputOTP
Item
Kbd
Label
Marker
Menubar
Message
MessageScroller
NativeSelect
NavigationMenu
Pagination
Popover
Progress
Questionnaire
RadioGroup
Resizable
ScrollArea
Select
Separator
Sheet
Sidebar
Skeleton
Slider
Spinner
Switch
Table
Tabs
Textarea
Toast
Toggle
ToggleGroup
Tooltip
Trace
Typography
Section
Grid
Stack
Container
```

```role-map
Accordion: group
Alert: alert
AlertDialog: alertdialog
AspectRatio: generic
Attachment: group
Avatar: img
Badge: generic
Breadcrumb: navigation
Bubble: generic
Button: button
ButtonGroup: group
Calendar: grid
Card: group
Carousel: region
Chart: img
Checkbox: checkbox
CodeBlock: code
Collapsible: group
Combobox: combobox
Command: dialog
ContextMenu: menu
DataTable: table
DatePicker: group
Dialog: dialog
Direction: generic
Drawer: dialog
DropdownMenu: menu
Empty: generic
Field: group
HoverCard: group
Input: textbox
InputGroup: group
InputOTP: group
Item: listitem
Kbd: code
Label: generic
Marker: mark
Menubar: menubar
Message: article
MessageScroller: log
NativeSelect: combobox
NavigationMenu: navigation
Pagination: navigation
Popover: dialog
Progress: progressbar
Questionnaire: form
RadioGroup: radiogroup
Resizable: group
ScrollArea: region
Select: combobox
Separator: separator
Sheet: dialog
Sidebar: complementary
Skeleton: generic
Slider: slider
Spinner: status
Switch: switch
Table: table
Tabs: tablist
Textarea: textbox
Toast: status
Toggle: button
ToggleGroup: group
Tooltip: tooltip
Trace: log
Typography: paragraph
Section: region
Grid: grid
Stack: group
Container: generic
```

Abstract roles (`command`, `widget`, `section`...) cấm dùng — W3C cấm tác giả dùng.
Role `generic`/`group` cho khung thuần trình bày là hợp lệ, không phải thiếu sót.
