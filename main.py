from pyscript import display, document

Grade_7 = {'Juan dela Cruz', 'Rene Baterbonia'}
Grade_8 = {'Jericho Magsalin', 'Jhoana Evangelista'}
Grade_9 = {'Gab Santos', 'Beaufort Oab', 'Maverick Carlos'}
Grade_10 = {'Elise Ramos', 'Cheree Mendoza', 'Therese Reyes','Zoey Ledres', 'Tyler Sales'}

def add_member(event):
  first_input = document.getElementById("first-name").value.strip().upper()
  last_input = document.getElementById("last-name").value.strip().upper()

  new_member_set = {f"{first_input} {last_input}"}

  all_members = Grade_7 | Grade_8 | Grade_9 | Grade_10 | new_member_set

  members_list = "<br>".join(sorted(all_members))

  total_members = len(all_members)

  output_html = (
      f"ALL MEMBERS:<br>{members_list}<br><br>TOTAL MEMBERS: {total_members}")
  document.getElementById("output-div").innerHTML = output_html
