# confluence/api.py

from atlassian import Confluence
import markdown2

def get_confluence_client(conf_cfg):
    return Confluence(
        url=conf_cfg["url"],
        username=conf_cfg["username"],
        password=conf_cfg["api_token"]
    )

def create_or_update_page(confluence, title, content_md, config, page_id=None):
    space = config["space_key"]
    parent_id = config.get("parent_page_id")
    html_body = markdown2.markdown(content_md)

    if page_id:
        try:
            confluence.update_page(
                page_id=page_id,
                title=title,
                body=html_body
            )
            return page_id
        except Exception as e:
            print(f"⚠️ 更新失败，将尝试创建新页面: {e}")

    page = confluence.get_page_by_title(space, title)
    if page:
        confluence.update_page(
            page_id=page["id"],
            title=title,
            body=html_body
        )
        return page["id"]
    else:
        new_page = confluence.create_page(
            space=space,
            title=title,
            body=html_body,
            parent_id=parent_id
        )
        return new_page["id"]
