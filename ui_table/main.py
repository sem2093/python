import pyto_ui as ui
import webbrowser

# The items
class Item:

    def __init__(self, title, subtitle):
        self.title = title
        self.subtitle = subtitle

    def cell(self):
        cell = ui.TableViewCell(ui.TABLE_VIEW_CELL_STYLE_SUBTITLE)
        cell.text_label.text = self.title
        cell.detail_text_label.text = self.subtitle
        cell.accessory_type = ui.ACCESSORY_TYPE_DISCLOSURE_INDICATOR
        cell.removable, cell.movable = True, True
        return cell

# The view opened when an item is pressed
class DeviceView(ui.View):
    
    def __init__(self, item):
        super().__init__()
        
        self.background_color = ui.COLOR_SYSTEM_BACKGROUND
    
        title_label = ui.Label(item.title)
        title_label.font = ui.Font.bold_system_font_of_size(40)
        title_label.size_to_fit()
        title_label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
        title_label.width = self.width
        title_label.flex = [ui.FLEXIBLE_WIDTH]
        title_label.y = 30
        self.add_subview(title_label)
    
        parts = item.title.split()
        url = "https://www.apple.com/"+parts[0].lower()
        try:
            url = url+"-"+parts[1].lower()
        except IndexError:
            pass
        self.url = url
    
        button = ui.Button(title="Show more")
        button.size_to_fit()
        button.y = title_label.y+(button.width*2)
        button.center_x = self.width/2
        button.flex = [
            ui.FLEXIBLE_BOTTOM_MARGIN,
            ui.FLEXIBLE_TOP_MARGIN,
            ui.FLEXIBLE_LEFT_MARGIN,
            ui.FLEXIBLE_RIGHT_MARGIN
        ]
        button.action = self.show_more
        self.add_subview(button)

    def show_more(self, button):
        webbrowser.open(self.url)

# The view listing the items
class TableView(ui.TableView):

    def __init__(self):        
        self.high = [
            Item("Task", "urgent"),
            Item("Task", "urgent"),
            Item("Task", "not urgent"),
            Item("Task", "not urgent"),
            Item("Task", "not urgent")
        ]
        
        self.medium = [
            Item("Task", "urgent"),
            Item("Task", "urgent"),
            Item("Task", "not urgent"),
            Item("Task", "not urgent"),
        ]
        
        self.low = [
            Item("Task", "urgent"),
            Item("Task", "urgent"),
            Item("Task", "not urgent"),
            Item("Task", "not urgent"),
            Item("Task", "not urgent")
        ]
        
        self.all_items = {
            ui.TableViewSection("High Priority", self.cells(self.high)) : self.high,  ui.TableViewSection("Medium Priority", self.cells(self.medium)) : self.medium,
            ui.TableViewSection("Low Priority", self.cells(self.low)) : self.low
        }
        
        super().__init__(sections=self.all_items.keys())
        self.button_items = [self.edit_button_item]
        
        for section in self.all_items.keys():
            section.did_select_cell = self.selected
            section.did_delete_cell = self.deleted
            section.did_move_cell = self.move

    def cells(self, items):
        cells = []
        for item in items:
            cells.append(item.cell())
        return cells

    def selected(self, section, cell_index):
        section.table_view.deselect_row()
        item = self.all_items[section][cell_index]
        
        view = DeviceView(item)
        section.table_view.push(view)
    
    def deleted(self, section, cell_index):
        self.all_items[section].pop(cell_index)
    
    def move(self, section, source_index, destination_index):
        item = self.all_items[section].pop(source_index)
        self.all_items[section].insert(destination_index, item)
    

# Show
table_view = TableView()
ui.show_view(table_view, ui.PRESENTATION_MODE_SHEET)
