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

function getCreatorList(){
    $.ajax({
        url: "/get_all_creators",
        type: "get",
        dataType: "json",
        data: 'data',
        success: function (data) {
            var area = document.getElementById("createBy");
            var optionstring = "";
            if (data.length > 0) {
                for (var i = 0; i < data.length; i++) {
                    optionstring += "<option>" + data[i] + "</option>"; //公共变量赋值
                }
            }

            if (area.options.length==0) {                 //如果下拉框没有数据才进行加载
                $("#createBy").html(optionstring);   //下拉框加载数据
                $('#createBy').selectpicker('refresh');
            }
        },

        error: function (data) {
            alert("查询学校失败" + data);
        }
    })
}
