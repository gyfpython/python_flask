function get_default_selection(element_id, option_id){
    m=$(element_id);
    let i;
    for(i=0;i<=m.options.length;i++)
        {
        if(parseInt(m.options[i].value)==parseInt(option_id))
            {
               m.options[i].selected=true;
               break;
            }
        }
}
function $(id){
     return document.getElementById(id);
}

function delete_entry_confirm(entry_id) {
    if (!confirm("delete confirm？")) {
        window.event.returnValue = false;
    }
    else{
        location.href=("/delete_entry/" + entry_id)
    }
}
